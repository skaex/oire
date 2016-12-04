from django.test import TestCase
from ..forms import OireAuthenticationForm, OirePasswordChangeForm, OirePasswordResetForm


class OireAuthenticationFormTest(TestCase):
    def setUp(self):
        self.form = OireAuthenticationForm()

    def test_username_field_has_right_placeholder(self):
        self.assertEqual(self.form.fields['username'].widget.attrs['placeholder'], 'e.g ****@aun.edu.ng')

    def test_username_field_has_right_css_classes(self):
        self.assertEqual(self.form.fields['username'].widget.attrs['class'], 'form-control')

    def test_username_field_has_right_label(self):
        self.assertEqual(self.form.fields['username'].label, 'AUN Email')

    def test_password_field_has_right_label(self):
        self.assertEqual(self.form.fields['password'].label, 'Password')

    def test_password_field_has_right_css_classes(self):
        self.assertEqual(self.form.fields['password'].widget.attrs['class'], 'form-control')

class OirePasswordChangeFormTest(TestCase):
    pass
    # I'll have to come back to this


class OirePasswordResetFormTest(TestCase):
    def setUp(self):
        self.form = OirePasswordResetForm()

    def test_email_field_has_right_placeholder(self):
        self.assertEqual(self.form.fields['email'].widget.attrs['placeholder'], 'e.g ****@aun.edu.ng')

    def test_email_field_has_right_css_classes(self):
        self.assertEqual(self.form.fields['email'].widget.attrs['class'], 'form-control')

    def test_email_field_has_auto_focus(self):
        self.assertEqual(self.form.fields['email'].widget.attrs['autofocus'], '')





