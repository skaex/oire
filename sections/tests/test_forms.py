from django.test import TestCase
from ..forms import (
    EMPTY_SEMESTER_YEAR_ERROR, EMPTY_SEMESTER_SEASON_ERROR,
    SemesterForm,
    SectionForm
)


class SemesterFormTest(TestCase):

    def test_form_has_placeholders_and_css_classes(self):
        form = SemesterForm()
        self.assertIn('placeholder="Enter a season"', form.as_p())
        self.assertIn('placeholder="Enter a year"', form.as_p())
        self.assertIn('class="form-control"', form.as_p())

    def test_form_validation_for_empty_semester_season(self):
        form = SemesterForm(data={'year': 2015, 'season': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['season'],
            [EMPTY_SEMESTER_SEASON_ERROR]
        )

    def test_form_validation_for_empty_semester_year(self):
        form = SemesterForm(data={'year': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['year'],
            [EMPTY_SEMESTER_YEAR_ERROR]
        )


class SectionFormTest(TestCase):
    def test_form_has_placeholders_and_css_classes(self):
        form = SectionForm()
        self.assertIn('placeholder="Enter the CRN"', form.as_p())
        self.assertIn('placeholder="Enter the class time', form.as_p())
        self.assertIn('placeholder="Enter the class location', form.as_p())
        self.assertIn('placeholder="Enter the class enrollment', form.as_p())
        self.assertIn('class="form-control"', form.as_p())
