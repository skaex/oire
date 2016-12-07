from django.test import TestCase
from ..forms import QuestionSetForm, EvaluationForm, CategoryForm, QuestionForm, EvaluateForm


class QuestionSetFormTest(TestCase):
    def test_form_has_placeholders_and_css_classes(self):
        form = QuestionSetForm()
        self.assertIn('placeholder="Enter a name for the question set. e.g 2014 Mid Semester Question Set"',
                      form.as_p())
        self.assertIn('class="form-control"', form.as_p())


class EvaluationFormTest(TestCase):
    def test_form_has_placeholders_and_css_classes(self):
        form = EvaluationForm()
        self.assertIn('placeholder="Enter a name for the evaluation. e.g 2014 Mid Semester"', form.as_p())
        self.assertIn('class="form-control"', form.as_p())


class CategoryFormTest(TestCase):
    def test_form_has_placeholders_and_css_classes(self):
        form = CategoryForm()
        self.assertIn('placeholder="Enter the category e.g Punctuality"', form.as_p())
        self.assertIn('class="form-control"', form.as_p())


class QuestionFormTest(TestCase):
    def test_form_has_placeholders_and_css_classes(self):
        form = QuestionForm()
        self.assertIn('placeholder="Enter the title of the question"', form.as_p())
        self.assertIn('placeholder="Enter the description of the question"', form.as_p())
        self.assertIn('placeholder="What position is the question **Please leave blank unless neccessary**"',
                      form.as_p())
        self.assertIn('class="form-control"', form.as_p())


class EvaluateFormTest(TestCase):
    def test_form_has_placeholders_and_css_classes(self):
        form = EvaluateForm()
        self.assertIn('class="form-control"', form.as_p())
