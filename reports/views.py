from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from django.views.defaults import page_not_found
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from braces.views import LoginRequiredMixin
from sections.models import Section
from evaluations.models import Evaluation, Question, Key
from .models import Response, Comment


class ReportListView(ListView, LoginRequiredMixin):
    model = Section
    template_name = 'reports/report/list.html'

    def get_queryset(self):
        qs = super(ReportListView, self).get_queryset()
        groups = self.request.user.groups.values_list("name", flat=True)
        try:
            page = self.request.GET['role']
        except Exception:

            if 'Faculty' in groups:
                return qs.filter(instructors=self.request.user)
            elif 'Special' in groups:
                return qs
            elif 'Dean' in groups:
                return qs.filter(course__school__school=self.request.user.school)
        else:
            if page == 'dean':
                if 'Dean' in groups:
                    return qs.filter(course__school__school=self.request.user.school)
            elif page == 'special':
                if 'Special' in groups:
                    return qs

        return qs.filter(instructors=self.request.user)


class ReportDetailView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        groups = self.request.user.groups.values_list("name", flat=True)
        section = Section.objects.get(id=self.kwargs['section'])
        if self.request.user.id not in section.instructors.values_list('id', flat=True)\
                and 'Special' not in groups and 'Dean' not in groups:
            return page_not_found(request)
        if 'Dean' in groups and self.request.user.school != section.course.school:
            return page_not_found(request)

        evaluation = Evaluation.objects.get(id=self.kwargs['evaluation'])
        responses = Response.objects.filter(section=section, evaluation=evaluation)
        comments = Comment.objects.filter(section=section, evaluation=evaluation)
        try:
            self.request.GET['printable']
        except Exception:
            return render(request, 'reports/report/detail.html', {'section': section,
                                                                  'evaluation': evaluation,
                                                                  'responses': responses,
                                                                  'comments': comments})
        else:
            return render(request, 'reports/report/printable.html', {'section': section,
                                                              'evaluation': evaluation,
                                                              'responses': responses,
                                                              'comments': comments})


class EvaluationSubmitView(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        entire_post = request.POST
        key = Key.objects.get(value=entire_post['key'])
        if key.status != Key.KEY_STATUSES[2][0]:
            section = Section.objects.get(id=kwargs['section'])
            evaluation = \
                Evaluation.objects.filter(semester=section.semester.id).filter(status=Evaluation.STATUSES[0][0])[0]
            for item in entire_post:
                if item.startswith('question'):
                    question = Question.objects.get(id=item.split('_')[1])
                    # Get response here and do increment.
                    response = Response.objects.get_or_create(
                        section=section,
                        evaluation=evaluation,
                        question=question
                    )
                    response = response[0]
                    if entire_post[item] == 'one':
                        response.one += 1
                    elif entire_post[item] == 'two':
                        response.two += 1
                    elif entire_post[item] == 'three':
                        response.three += 1
                    elif entire_post[item] == 'four':
                        response.four += 1
                    elif entire_post[item] == 'five':
                        response.five += 1
                    else:
                        pass
                    response.save()
            if entire_post['comment']:
                Comment.objects.create(
                    comment=entire_post['comment'],
                    section=section,
                    evaluation=evaluation)
            key = Key.objects.get(value=entire_post['key'])
            key.status = Key.KEY_STATUSES[2][0]
            key.save()
            section.status = Section.STATUSES[2][0]
            section.save()
            messages.success(request, 'Thank you!!! Your response has been recieved.')
            return redirect(reverse_lazy('credits'))
        messages.error(request, "Something doesn't seem right here. A key is meant for only one submission.",
                       extra_tags="danger")
        return redirect(reverse_lazy('evaluate'))


class CreditsView(TemplateView):
    template_name = 'reports/display/credits.html'
