from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import QuestionSet, Evaluation, Question, Category, Key
from .forms import QuestionSetForm, EvaluationForm, CategoryForm, QuestionForm, EvaluateForm
from sections.models import Section


class QuestionSetMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = QuestionSet


class QuestionSetEditMixin(QuestionSetMixin):
    template_name = 'evaluations/management/questionset/form.html'
    form_class = QuestionSetForm
    success_url = reverse_lazy('questionset_list')


class QuestionSetListView(QuestionSetMixin, ListView):
    template_name = 'evaluations/management/questionset/list.html'
    paginate_by = 10


class QuestionSetAddView(QuestionSetEditMixin, CreateView):
    success_message = "%(name)s was created successfully"


class QuestionSetUpdateView(QuestionSetEditMixin, UpdateView):
    success_message = "%(name)s was updated successfully"


class EvaluationMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Evaluation


class EvaluationEditMixin(EvaluationMixin):
    template_name = 'evaluations/management/evaluation/form.html'
    form_class = EvaluationForm
    success_url = reverse_lazy('evaluation_list')


class EvaluationListView(EvaluationMixin, ListView):
    template_name = 'evaluations/management/evaluation/list.html'
    paginate_by = 10


class EvaluationAddView(EvaluationEditMixin, CreateView):
    success_message = "%(name)s was created successfully"


class EvaluationUpdateView(EvaluationEditMixin, UpdateView):
    success_message = "%(name)s was updated successfully"


class EvaluationOpenView(LoginRequiredMixin, View):

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        open_evaluation = Evaluation.objects.filter(status=Evaluation.STATUSES[0][0])
        if not open_evaluation:
            # Wrap these in a transaction
            evaluation = Evaluation.objects.get(id=kwargs['eval'])
            evaluation.status = Evaluation.STATUSES[0][0]
            evaluation.save()
            # Set all sections here ready.
            evaluation.semester.section_set.update(status=Section.STATUSES[1][0])

            messages.success(request, '%s was started successfully' % (evaluation.name))
        return redirect(reverse_lazy('evaluation_list'))


class EvaluationFinishView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        evaluation = Evaluation.objects.get(id=kwargs['eval'])
        evaluation.status = Evaluation.STATUSES[2][0]
        evaluation.save()
        messages.success(request, '%s was finished successfully' % (evaluation.name))
        return redirect(reverse_lazy('evaluation_list'))


class CategoryEditMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Category
    template_name = 'evaluations/management/category/form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('questionset_list')


class CategoryAddView(CategoryEditMixin, CreateView):
    success_message = "%(name)s was created successfully"


class CategoryUpdateView(CategoryEditMixin, UpdateView):
    success_message = "%(name)s was updated successfully"


class QuestionMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Question


class QuestionEditMixin(QuestionMixin):
    template_name = 'evaluations/management/question/form.html'
    form_class = QuestionForm
    success_url = reverse_lazy('questionset_list')


class QuestionAddView(QuestionEditMixin, CreateView):
    success_message = "%(title)s was created successfully"


class QuestionUpdateView(QuestionEditMixin, UpdateView):
    success_message = "%(title)s was updated successfully"


class QuestionListView(QuestionMixin, ListView):
    template_name = 'evaluations/management/question/list.html'
    paginate_by = 10


class KeySectionListView(LoginRequiredMixin, ListView):
    model = Key
    template_name = 'evaluations/management/key/list.html'

    def get_queryset(self):
        qs = super(KeySectionListView, self).get_queryset()
        return qs.filter(section=self.kwargs['sec'])


WRONG_KEY_ERROR = "It seems the key was wrong"
USED_KEY_ERROR = "It seems the key has been used"


class EvaluateFormView(View):
    form_class = EvaluateForm
    template_name = 'evaluations/evaluate/form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                key = Key.objects.get(value=form.data['key'])
            except Exception:
                form.errors['error'] = WRONG_KEY_ERROR
            else:
                if key.status == Key.KEY_STATUSES[2][0]:
                    form.errors['error'] = USED_KEY_ERROR
                elif key.helper:
                    keys = Key.objects.filter(section=key.section.id, evaluation=key.evaluation.id, helper=False)
                    key.status = Key.KEY_STATUSES[1][0]
                    key.save()
                    return render(request, 'evaluations/evaluate/section_keys.html',
                                  {'keys': keys, 'section': key.section})

                else:
                    categories = key.evaluation.question_set.category_set.all()
                    key.status = Key.KEY_STATUSES[1][0]
                    key.save()
                    return render(request, 'evaluations/evaluate/evaluation_form.html',
                                  {'categories': categories, 'key': key})
            return render(request, self.template_name, {'form': form})

            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})
