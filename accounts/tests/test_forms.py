from django.test import TestCase
from ..forms import OireAuthenticationForm, OirePasswordChangeForm, OirePasswordResetForm, UserAddForm, UserEditForm


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


class UserAddFormTest(TestCase):
    def setUp(self):
        self.form = UserAddForm()

    def test_first_name_has_right_placeholder(self):
        self.assertEqual(self.form.fields['first_name'].widget.attrs['placeholder'], 'Enter a first name')

    def test_first_name_has_right_css_class(self):
        self.assertEqual(self.form.fields['first_name'].widget.attrs['class'], 'form-control')

    def test_last_name_has_right_placeholder(self):
        self.assertEqual(self.form.fields['last_name'].widget.attrs['placeholder'], 'Enter a last name')

    def test_last_name_has_right_css_class(self):
        self.assertEqual(self.form.fields['last_name'].widget.attrs['class'], 'form-control')

    def test_email_has_right_placeholder(self):
        self.assertEqual(self.form.fields['email'].widget.attrs['placeholder'], 'Enter an email')

    def test_email_has_right_css_class(self):
        self.assertEqual(self.form.fields['email'].widget.attrs['class'], 'form-control')

    def test_school_has_right_css_class(self):
        self.assertEqual(self.form.fields['school'].widget.attrs['class'], 'form-control')


class UserEditFormTest(UserAddFormTest):
    def setUp(self):
        self.form = UserEditForm()

    # I can see this is redundant
    def test_user_permissions_field_exists_in_form(self):
        self.assertTrue('user_permissions' in self.form.fields)

    def test_user_permissions_field_has_right_css_class(self):
        self.assertEqual(self.form.fields['user_permissions'].widget.attrs['class'], 'form-control')

    def test_is_active_field_exists_in_form(self):
        self.assertTrue('is_active' in self.form.fields)
