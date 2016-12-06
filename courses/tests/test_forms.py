from django.test import TestCase
from .factories import SchoolFactory
from ..forms import (
    EMPTY_SCHOOL_ERROR, SchoolForm,
    EMPTY_COURSE_CODE_ERROR, EMPTY_COURSE_TITLE_ERROR, EMPTY_COURSE_SCHOOL_ERROR,
    CourseForm
)


class SchoolFormTest(TestCase):
    def setUp(self):
        self.form = SchoolForm()

    def test_school_field_exists_in_form(self):
        self.assertTrue('school' in self.form.fields)

    def test_school_has_right_css_class(self):
        self.assertEqual(self.form.fields['school'].widget.attrs['class'], 'form-control')

    def test_school_has_right_placeholder(self):
        self.assertEqual(self.form.fields['school'].widget.attrs['placeholder'], 'Enter a school name')

    def test_school_description_field_exists_in_form(self):
        self.assertTrue('description' in self.form.fields)

    def test_school_description_has_right_css_class(self):
        self.assertEqual(self.form.fields['description'].widget.attrs['class'], 'form-control')

    def test_school_description_has_right_placeholder(self):
        self.assertEqual(self.form.fields['description'].widget.attrs['placeholder'], 'Describe the school')

    def test_form_validation_for_empty_school(self):
        form = SchoolForm(data={'school': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['school'],
            [EMPTY_SCHOOL_ERROR]
        )

    def test_form_novalidate_for_empty_description(self):
        form = SchoolForm(data={'school': 'sitc', 'description': ''})
        self.assertTrue(form.is_valid())


class CourseFormTest(TestCase):
    def setUp(self):
        self.school = SchoolFactory.create()
        self.form = CourseForm()

    def test_course_code_field_exists_in_form(self):
        self.assertTrue('code' in self.form.fields)

    def test_course_code_has_right_css_class(self):
        self.assertEqual(self.form.fields['code'].widget.attrs['class'], 'form-control')

    def test_course_code_has_right_placeholder(self):
        self.assertEqual(self.form.fields['code'].widget.attrs['placeholder'], 'Enter a course code')

    # I'll come back and finish up these

    def test_form_has_placeholders_and_css_classes(self):
        # This has to go
        self.assertIn('placeholder="Enter a course code', self.form.as_p())
        self.assertIn('placeholder="Enter a course title', self.form.as_p())
        self.assertIn('placeholder="Enter a course description', self.form.as_p())
        self.assertIn('class="form-control"', self.form.as_p())

    def test_form_validation_for_empty_code(self):
        form = CourseForm(data={'title': 'coa', 'discription': 'sd', 'school': self.school.id})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['code'],
            [EMPTY_COURSE_CODE_ERROR]
        )

    def test_form_validation_for_empty_title(self):
        form = CourseForm(data={'code': 'csc232', 'discription': 'sd', 'school': self.school.id})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['title'],
            [EMPTY_COURSE_TITLE_ERROR]
        )

    def test_form_validation_for_empty_school(self):
        form = CourseForm(data={'code': 'csc232', 'title': 'coa', 'discription': 'sd', })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['school'],
            [EMPTY_COURSE_SCHOOL_ERROR]
        )


