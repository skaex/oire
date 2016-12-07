from django.core.exceptions import ValidationError
from django.test import TestCase
from ..models import Semester, Section
from .factories import SemesterFactory, SectionFactory


class SemesterModelTest(TestCase):
    def setUp(self):
        self.factory = SemesterFactory

    def test_can_create_semester(self):
        semester = self.factory.create()
        self.assertEqual(list(Semester.objects.all()), [semester, ])

    # Don't you wonder what order the ORM gets these objects?
    #
    def test_string_representation(self):
        semester = self.factory.build()
        self.assertEqual(str(semester), '%s %s' % (semester.season, semester.year))

    def test_default_is_current_attr(self):
        semester = self.factory.build()
        self.assertEqual(semester.is_current, False)

    def test_duplicate_semesters_are_not_allowed(self):
        semester_1 = self.factory.create()
        with self.assertRaises(ValidationError):
            semester_2 = Semester(season=semester_1.season, year=semester_1.year)
            semester_2.full_clean()


class SectionModelTest(TestCase):
    def setUp(self):
        self.factory = SectionFactory

    def test_can_create_section(self):
        section = self.factory.create()
        self.assertEqual(list(Section.objects.all()), [section, ])

    def test_string_respresentation_of_section(self):
        section = self.factory.create()
        self.assertEqual(str(section), section.crn)
