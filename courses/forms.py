from django import forms
from .models import School, Course

EMPTY_SCHOOL_ERROR = "You have to provide a school name"


class SchoolForm(forms.models.ModelForm):
    class Meta:
        model = School
        fields = ('school', 'description')
        widgets = {
            'school': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a school name',
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the school',
                'class': 'form-control',
            })
        }
        error_messages = {
            'school': {'required': EMPTY_SCHOOL_ERROR}
        }


EMPTY_COURSE_CODE_ERROR = "You have to provide a course code"
EMPTY_COURSE_TITLE_ERROR = "You have to provide a course title"
EMPTY_COURSE_SCHOOL_ERROR = "You have to provide a course school"


class CourseForm(forms.models.ModelForm):
    class Meta:
        model = Course
        fields = ('code', 'title', 'school', 'description')
        widgets = {
            'code': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a course code',
                'class': 'form-control',
            }),
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a course title',
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter a course description',
                'class': 'form-control',
            }),
            'school': forms.fields.Select(attrs={
                'class': 'form-control',
            }),
        }
        error_messages = {
            'code': {'required': EMPTY_COURSE_CODE_ERROR},
            'title': {'required': EMPTY_COURSE_TITLE_ERROR},
            'school': {'required': EMPTY_COURSE_SCHOOL_ERROR},
        }
