from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Semester, Section
from .forms import SemesterForm, SectionForm


class SemesterMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Semester


class SemesterEditMixin(SemesterMixin):
    template_name = 'sections/management/semester/form.html'
    form_class = SemesterForm
    success_url = reverse_lazy('semester_list')


class SemesterListView(SemesterMixin, ListView):
    # I'm too lazy to figure the below out
    template_name = 'sections/management/semester/list.html'
    paginate_by = 10


class SemesterAddView(SemesterEditMixin, CreateView):
    success_message = "%(season)s %(year)s was created successfully"


class SemesterUpdateView(SemesterEditMixin, UpdateView):
    success_message = "%(season)s %(year)s was updated successfully"


class SemesterDeleteView(SemesterMixin, DeleteView):
    success_url = reverse_lazy('semester_list')
    template_name = 'sections/management/semester/delete.html'
    success_message = "%(season)s %(year)s was deleted successfully"


class SectionMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Section


class SectionEditMixin(SectionMixin):
    template_name = 'sections/management/section/form.html'
    form_class = SectionForm
    success_url = reverse_lazy('section_list')


class SectionListView(SectionMixin, ListView):
    template_name = 'sections/management/section/list.html'
    paginate_by = 10


class SectionAddView(SectionEditMixin, CreateView):
    success_message = "%(crn)s was created successfully"


class SectionUpdateView(SectionEditMixin, UpdateView):
    success_message = "%(crn)s was updated successfully"


class SectionDeleteView(SectionMixin, DeleteView):
    success_url = reverse_lazy('section_list')
    template_name = 'sections/management/section/delete.html'
    success_message = "%(crn)s was deleted successfully"

