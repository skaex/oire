from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Semester, Section, PreSection
from courses.models import Course
from accounts.models import User
from evaluations.models import Key
from sections.forms import SemesterForm, SectionForm, PreSectionForm, PreSectionsFileUploadForm
from sections.repositories import SectionRepository


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
        repository = SectionRepository()
        if repository.open_section(section):
            messages.success(request, '%s opened successfully' % (section.crn))
        else:
            messages.error(request, '%s was not opened successfully' % (section.crn))
        return redirect(reverse_lazy('section_list'))


class SectionCloseView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sections.change_section'

    def get(self, request, *args, **kwargs):
        section = Section.objects.get(id=kwargs['section'])
        repository = SectionRepository()
        if repository.close_section(section):
            messages.success(request, 'Operation on %s was successful' % (section.crn))
        else:
            messages.error(request, 'Operation on %s was not successful' % (section.crn))
        return redirect(reverse_lazy('section_list'))


class SectionLoadView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sections.change_section'

    def get(self, request):
        if PreSection.objects.count() == PreSection.objects.filter(error_column="").count():
            pre_sections = PreSection.objects.all()
            for pre_section in pre_sections:
                ncourse = Course.objects.get(code=pre_section.course)
                smstr = pre_section.semester.split(' ')
                nsemester = Semester.objects.get(season=smstr[0], year=smstr[1])
                section = Section.objects.create(
                        crn=pre_section.crn,
                        course=ncourse,
                        time=pre_section.time,
                        location=pre_section.location,
                        enrolled=pre_section.enrolled,
                        semester=nsemester
                    )
                instrs = pre_section.instructors.split(', ')
                for instr in instrs:
                    section.instructors.add(User.objects.get(email=instr))
            PreSection.objects.all().delete()
            messages.success(request, 'Operation was successfully!')
            return redirect(reverse_lazy('presection_list'))
        messages.error(request, 'Operation was not successful!! There were some erroneous presections')
        return redirect(reverse_lazy('presection_list'))


class PreSectionMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = PreSection


class PreSectionEditMixin(PreSectionMixin):
    template_name = 'sections/management/presection/form.html'
    form_class = PreSectionForm
    success_url = reverse_lazy('presection_list')


class PreSectionListView(PermissionRequiredMixin, PreSectionMixin, ListView):
    permission_required = 'sections.change_presection'
    template_name = 'sections/management/presection/list.html'
    paginate_by = 10


class PreSectionAddView(PermissionRequiredMixin, PreSectionEditMixin, CreateView):
    permission_required = 'sections.add_presection'
    success_message = "PRE-SECTION %(crn)s was created successfully"


class PreSectionUpdateView(PermissionRequiredMixin, PreSectionEditMixin, UpdateView):
    permission_required = 'sections.change_presection'
    success_message = "PRE-SECTION %(crn)s was updated successfully"


class PreSectionDeleteView(PermissionRequiredMixin, PreSectionMixin, DeleteView):
    permission_required = 'sections.delete_presection'
    success_url = reverse_lazy('presection_list')
    template_name = 'sections/management/presection/delete.html'
    success_message = "PRE-SECTION %(crn)s was deleted successfully"


class PreSectionRefreshView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sections.change_presection'

    def get(self, request, *args, **kwargs):
        pre_section = PreSection.objects.get(id=kwargs['presection'])
        pre_section.crn = pre_section.crn
        pre_section.save()
        messages.success(request, 'Operation REFRESH on PRE-SECTION %s was successful' % (pre_section.crn))
        return redirect(reverse_lazy('presection_list'))


class PreSectionLoadView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sections.change_presection'
    form_class = PreSectionsFileUploadForm
    template_name = 'sections/management/presection/loading_form.html'

    def get(self, request, *args, **kwargs):
        form = PreSectionsFileUploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PreSectionsFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            items = request.FILES['file'].get_array()
            for idx in range(len(items)):
                if idx == 0:
                    continue
                item = items[idx]
                PreSection.objects.create(
                    crn=item[0],
                    course=item[1],
                    time=item[2],
                    location=item[3],
                    instructors=item[4],
                    enrolled=item[5],
                    semester=item[6]
                )

            messages.success(request, 'Loading Operation on PRE-SECTION was successful')
            return redirect(reverse_lazy('presection_list'))
        messages.error(request, 'Loading Operation on PRE-SECTION was not successful')
        return redirect(reverse_lazy('load_presections'))