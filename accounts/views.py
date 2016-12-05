from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.hashers import make_password
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import DEFAULT_USER_PASSWORD
from .forms import UserAddForm, UserEditForm


class UserMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = User


class UserEditMixin(UserMixin):
    template_name = 'accounts/management/user/form.html'
    success_url = reverse_lazy('user_list')


class UserListView(UserMixin, ListView):
    template_name = 'accounts/management/user/list.html'
    paginate_by = 10


class UserAddView(UserEditMixin, CreateView):
    success_message = "%(email)s was created successfully"
    # Lets do some overide
    form_class = UserAddForm

    def form_valid(self, form):
        form.instance.password = make_password(DEFAULT_USER_PASSWORD)
        form.instance.username = form.instance.email.split('@')[0]
        return super(UserAddView, self).form_valid(form)


class UserUpdateView(UserEditMixin, UpdateView):
    form_class = UserEditForm
    success_message = "%(email)s was updated successfully"
