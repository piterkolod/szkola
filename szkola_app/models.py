from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SCHOOL_CLASS = (
    (1, "1a"),
    (2, "1b"),
    (3, "1c"),
    (4, "2a"),
    (5, "2b"),
    (6, "2c"),
    (7, "3a"),
    (8, "3b"),
    (9, "3c"),
    (10, "4a"),
    (11, "4b"),
    (12, "4c")
)

GRADES = (
    (1, "1"),
    (1.5, "1+"),
    (1.75, "2-"),
    (2, "2"),
    (2.5, "2+"),
    (2.75, "3-"),
    (3, "3"),
    (3.5, "3+"),
    (3.75, "4-"),
    (4, "4"),
    (4.5, "4+"),
    (4.75, "5-"),
    (5, "5"),
    (5.5, "5+"),
    (5.75, "6-"),
    (6, "6")
)

class SchoolSubject(models.Model):
    name = models.CharField(max_length=32, verbose_name="Nazwa przedmiotu")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, default=None)
    first_name = models.CharField(max_length=32, verbose_name="Imię nauczyciela")
    last_name =  models.CharField(max_length=64, verbose_name="Nazwisko nauczyciela")
    school_subject = models.ForeignKey(SchoolSubject)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.school_subject)


class SchoolClass(models.Model):
    number = models.IntegerField(choices =SCHOOL_CLASS)
    teacher = models.OneToOneField(Teacher)

    def __str__(self):
        return "{} {}".format(self.number, self.teacher)


class Student(models.Model):
    user = models.OneToOneField(User, null=True, default=None)
    first_name = models.CharField(max_length=32, verbose_name="Imię studenta")
    last_name =  models.CharField(max_length=64, verbose_name="Nazwisko studenta")
    school_class = models.ForeignKey(SchoolClass)
    grades = models.ManyToManyField(SchoolSubject, through="StudentGrades")

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)


class StudentGrades(models.Model):
    student = models.ForeignKey(Student)
    school_subject = models.ForeignKey(SchoolSubject)
    grade = models.FloatField(choices=GRADES)

    def __str__(self):
        return '{} {} {}'.format(self.student, self.school_subject, self.grade)