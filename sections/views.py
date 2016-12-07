from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Semester, Section
from evaluations.models import Key
from sections.forms import SemesterForm, SectionForm
from evaluations.repositories import KeyRepository


class SemesterMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Semester


class SemesterEditMixin(SemesterMixin):
    template_name = 'sections/management/semester/form.html'
    form_class = SemesterForm
    success_url = reverse_lazy('semester_list')


class SemesterListView(PermissionRequiredMixin, SemesterMixin, ListView):
    # I'm too lazy to figure the below out
    permission_required = 'sections.change_semester'
    template_name = 'sections/management/semester/list.html'
    paginate_by = 10


class SemesterAddView(PermissionRequiredMixin, SemesterEditMixin, CreateView):
    permission_required = 'sections.add_semester'
    success_message = "%(season)s %(year)s was created successfully"


class SemesterUpdateView(PermissionRequiredMixin, SemesterEditMixin, UpdateView):
    permission_required = 'sections.change_semester'
    success_message = "%(season)s %(year)s was updated successfully"


class SemesterDeleteView(PermissionRequiredMixin, SemesterMixin, DeleteView):
    permission_required = 'sections.delete_semester'
    success_url = reverse_lazy('semester_list')
    template_name = 'sections/management/semester/delete.html'
    success_message = "%(season)s %(year)s was deleted successfully"


class HelperListView(ListView):
    model = Key
    template_name = 'sections/management/helper/list.html'

    def get_queryset(self):
        qs = super(HelperListView, self).get_queryset()
        return qs.filter(helper=True)


class SectionMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Section


class SectionEditMixin(SectionMixin):
    template_name = 'sections/management/section/form.html'
    form_class = SectionForm
    success_url = reverse_lazy('section_list')


class SectionListView(PermissionRequiredMixin, SectionMixin, ListView):
    permission_required = 'sections.change_section'
    template_name = 'sections/management/section/list.html'
    paginate_by = 10


class SectionAddView(PermissionRequiredMixin, SectionEditMixin, CreateView):
    permission_required = 'sections.add_section'
    success_message = "%(crn)s was created successfully"


class SectionUpdateView(PermissionRequiredMixin, SectionEditMixin, UpdateView):
    permission_required = 'sections.change_section'
    success_message = "%(crn)s was updated successfully"


class SectionDeleteView(PermissionRequiredMixin, SectionMixin, DeleteView):
    permission_required = 'sections.delete_section'
    success_url = reverse_lazy('section_list')
    template_name = 'sections/management/section/delete.html'
    success_message = "%(crn)s was deleted successfully"


class SectionOpenView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sections.change_section'

    def get(self, request, *args, **kwargs):
        section = Section.objects.get(id=kwargs['section'])
        key_repo = KeyRepository()
        if section.status == Section.STATUSES[1][0]:
            key_repo.create_keys(section)
            section.status = Section.STATUSES[0][0]
        section.save()
        messages.success(request, '%s opened successfully' % (section.crn))
        return redirect(reverse_lazy('section_list'))


class SectionCloseView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sections.change_section'

    def get(self, request, *args, **kwargs):
        section = Section.objects.get(id=kwargs['section'])
        if section.status == Section.STATUSES[0][0]:
            key_repo = KeyRepository()
            key_repo.delete_keys(section)
            section.status = Section.STATUSES[1][0]
            messages.success(request, '%s locked successfully' % (section.crn))
        elif section.status == Section.STATUSES[2][0]:
            key_repo = KeyRepository()
            key_repo.delete_keys(section)
            section.status = Section.STATUSES[3][0]
            messages.success(request, '%s closed successfully' % (section.crn))
        else:
            section.status = section.status
        section.save()
        return redirect(reverse_lazy('section_list'))


class SectionLoadView(View):
    pass

