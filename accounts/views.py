from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, PasswordResetView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import DEFAULT_USER_PASSWORD, User
from .forms import UserAddForm, UserEditForm, OireAuthenticationForm, OirePasswordResetForm

class OireLoginView(LoginView):
    authentication_form = OireAuthenticationForm

class OirePasswordResetView(PasswordResetView):
    form_class = OirePasswordResetForm

class UserMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = User


class UserEditMixin(UserMixin):
    template_name = 'accounts/management/user/form.html'
    success_url = reverse_lazy('user_list')


class UserListView(PermissionRequiredMixin, UserMixin, ListView):
    permission_required = 'auth.change_user'
    template_name = 'accounts/management/user/list.html'
    paginate_by = 10


class UserAddView(PermissionRequiredMixin, UserEditMixin, CreateView):
    permission_required = 'auth.add_user'
    success_message = "%(email)s was created successfully"
    # Lets do some overide
    form_class = UserAddForm

    def form_valid(self, form):
        form.instance.password = make_password(DEFAULT_USER_PASSWORD)
        form.instance.username = form.instance.email.split('@')[0]
        return super(UserAddView, self).form_valid(form)


class UserUpdateView(PermissionRequiredMixin, UserEditMixin, UpdateView):
    permission_required = 'auth.change_user'
    form_class = UserEditForm
    success_message = "%(email)s was updated successfully"
