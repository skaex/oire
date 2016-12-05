from django.test import TestCase
from ..forms import UserAddForm, UserEditForm
from .factories import UserFactory
from ..models import TESTING_PASSWORD


class AuthViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.client.login(username=self.user.username, password=TESTING_PASSWORD)


class UserViewTest(AuthViewTest):
    def test_list_users_renders_right_template(self):
        response = self.client.get('/accounts/users/')
        self.assertTemplateUsed(response, 'accounts/management/user/list.html')

    def test_add_users_uses_right_form(self):
        response = self.client.get('/accounts/users/new/')
        self.assertIsInstance(response.context['form'], UserAddForm)

    def test_edit_users_users_right_form(self):
        response = self.client.get('/accounts/users/%d/edit/' % (self.user.id))
        self.assertIsInstance(response.context['form'], UserEditForm)