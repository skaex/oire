from django.core.exceptions import ValidationError
from django.test import TestCase
from ..models import School, Course
from .factories import SchoolFactory, CourseFactory


class SchoolModelTest(TestCase):
    def setUp(self):
        self.factory = SchoolFactory

    def test_string_representation(self):
        school = self.factory.build()
        self.assertEqual(str(school), school.school)

    def test_can_create_school(self):
        school = self.factory.create()
        self.assertEqual(list(School.objects.all()), [school, ])

    def test_default_description_attr(self):
        school = self.factory.build()
        self.assertEqual(school.description, '')  # I wish i could do away with the string

        # I would have written code to test editing and deleting the model
        # However, I did not write the code logic for all these.
        #


class CourseModelTest(TestCase):
    def setUp(self):
        self.factory = CourseFactory

    def test_string_representation(self):
        course = self.factory.build()
        self.assertEqual(str(course), course.code)

    def test_can_create_course(self):
        course = self.factory.create()
        self.assertEqual(list(Course.objects.all()), [course, ])

    def test_empty_course_code_is_not_allowed(self):
        with self.assertRaises(ValidationError):
            course = self.factory.build()
            course.code = None
            course.full_clean()

    def test_empty_course_title_is_not_allowed(self):
        with self.assertRaises(ValidationError):
            course = self.factory.build()
            course.title = None
            course.full_clean()

    def test_course_is_related_to_school(self):
        school = SchoolFactory.create()
        course = self.factory.build()
        course.school = school
        course.save()
        self.assertIn(course, school.course_set.all())
