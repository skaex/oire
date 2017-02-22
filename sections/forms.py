from django import forms
from .models import Semester, Section, PreSection

EMPTY_SEMESTER_SEASON_ERROR = "You have to provide a semester season"
EMPTY_SEMESTER_YEAR_ERROR = "You have to provide a semester year"


class SemesterForm(forms.models.ModelForm):
    class Meta:
        model = Semester
        fields = ('season', 'year')
        widgets = {
            'season': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a season',
                'class': 'form-control',
            }),
            'year': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a year',
                'class': 'form-control',
            })
        }
        error_messages = {
            'season': {'required': EMPTY_SEMESTER_SEASON_ERROR},
            'year': {'required': EMPTY_SEMESTER_YEAR_ERROR}
        }


class SectionForm(forms.models.ModelForm):
    class Meta:
        model = Section
        fields = ('crn', 'course', 'semester', 'time', 'location', 'enrolled', 'instructors')
        widgets = {
            'crn': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the CRN',
                'class': 'form-control',
            }),
            'course': forms.fields.Select(attrs={
                'class': 'form-control'
            }),
            'semester': forms.fields.Select(attrs={
                'class': 'form-control'
            }),
            'time': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the class time',
                'class': 'form-control',
            }),
            'location': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the class location',
                'class': 'form-control',
            }),
            'enrolled': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the class enrollment',
                'class': 'form-control',
            }),
            'instructors': forms.fields.SelectMultiple(attrs={
                'class': 'form-control'
            })

        }
        labels = {
            'crn': 'CRN'
        }


class PreSectionForm(forms.models.ModelForm):
    class Meta:
        model = PreSection
        fields = ('crn', 'course', 'semester', 'time', 'location', 'enrolled', 'instructors')
        widgets = {
            'crn': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the CRN',
                'class': 'form-control',
            }),
            'course': forms.fields.TextInput(attrs={
                'class': 'form-control'
            }),
            'semester': forms.fields.TextInput(attrs={
                'class': 'form-control'
            }),
            'time': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the class time',
                'class': 'form-control',
            }),
            'location': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the class location',
                'class': 'form-control',
            }),
            'enrolled': forms.fields.TextInput(attrs={
                'placeholder': 'Enter the class enrollment',
                'class': 'form-control',
            }),
            'instructors': forms.fields.TextInput(attrs={
                'class': 'form-control'
            })

        }
        labels = {
            'crn': 'CRN'
        }


class PreSectionsFileUploadForm(forms.Form):
    file = forms.FileField(label=("Evaluation File: XLS | CSV | XLSX"), widget=forms.FileInput(attrs={
                              'class': 'form-control',
                              'required': 'required'
                          }))
