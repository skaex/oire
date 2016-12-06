from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import School, Course
from .forms import SchoolForm, CourseForm


class SchoolMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = School


class SchoolEditMixin(SchoolMixin):
    template_name = 'courses/management/school/form.html'
    form_class = SchoolForm
    success_url = reverse_lazy('school_list')


class SchoolListView(SchoolMixin, ListView):
    template_name = 'courses/management/school/list.html'
    paginate_by = 10


class SchoolAddView(SchoolEditMixin, CreateView):
    success_message = "%(school)s was created successfully"


class SchoolUpdateView(SchoolEditMixin, UpdateView):
    success_message = "%(school)s was updated successfully"


# TODO: I don't think there should be a delete view here. I'll just leave
# it in for debugging purposes.
class SchoolDeleteView(SchoolMixin, DeleteView):
    success_url = reverse_lazy('school_list')
    template_name = 'courses/management/school/delete.html'
    success_message = "%(school)s was deleted successfully"


class CourseMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Course


class CourseEditMixin(CourseMixin, SuccessMessageMixin):
    template_name = 'courses/management/course/form.html'
    form_class = CourseForm
    success_url = reverse_lazy('course_list')


class CourseListView(CourseMixin, ListView):
    template_name = 'courses/management/course/list.html'
    paginate_by = 10


class CourseAddView(CourseEditMixin, CreateView):
    success_message = "%(code)s was deleted successfully"


class CourseUpdateView(CourseEditMixin, UpdateView):
    success_message = "%(code)s was updated successfully"


# TODO: I don't think there should be a delete view here too
class CourseDeleteView(CourseMixin, DeleteView):
    success_url = reverse_lazy('course_list')
    template_name = 'courses/management/course/delete.html'
    success_message = "%(code)s was deleted successfully"
