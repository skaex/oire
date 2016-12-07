from django import forms
from .models import QuestionSet, Evaluation, Category, Question


class EvaluationForm(forms.models.ModelForm):
    class Meta:
        model = Evaluation
        fields = ('name', 'semester', 'question_set', 'special')
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a name for the evaluation. e.g 2014 Mid Semester',
                'class': 'form-control',
            }),
            'semester': forms.fields.Select(attrs={
                'class': 'form-control',
            }),
            'question_set': forms.fields.Select(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'question_set': 'Question Set'
        }


class QuestionSetForm(forms.models.ModelForm):
    class Meta:
        model = QuestionSet
        fields = ('name',)
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a name for the question set. e.g 2014 Mid Semester Question Set',
                'class': 'form-control',
            }),
        }
        labels = {
            'name': 'Question Set'
        }


class CategoryForm(forms.models.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'question_set')
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the category e.g Punctuality',
                'class': 'form-control',
            }),
            'question_set': forms.fields.Select(attrs={
                'class': 'form-control',
            }),

        }


class QuestionForm(forms.models.ModelForm):
    class Meta:
        model = Question
        fields = ('category', 'title', 'description', 'order')
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the title of the question',
                'class': 'form-control',
            }),
            'category': forms.fields.Select(attrs={
                'class': 'form-control',
            }),
            'description': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the description of the question',
                'class': 'form-control',
            }),
            'order': forms.fields.TextInput(attrs={
                'placeholder': 'What position is the question **Please leave blank unless neccessary**',
                'class': 'form-control',
            }),

        }
        help_texts = {
            'order': 'Please leave blank unless neccessary.'
        }


class EvaluateForm(forms.Form):
    key = forms.CharField(required=False, label=("Evaluation key"),
                          widget=forms.fields.TextInput(attrs={
                              'class': 'form-control',
                              'required': 'required'
                          }))
