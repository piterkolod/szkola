from django.test import TestCase
from szkola_app.models import *

# Create your tests here.


class SchoolSubjectTestCase(TestCase):
    def test_string_representation(self):
        math = SchoolSubject.objects.create(name="matematyka")
        self.assertEqual(str(math), math.name)


class TeacherTestCase(TestCase):
    def test_string_representation(self):
        math = SchoolSubject.objects.create(name="matematyka")
        teacher = Teacher.objects.create(first_name="Jan", last_name="Janowski", school_subject=math)
        self.assertEqual(str(teacher), "Jan Janowski matematyka")
