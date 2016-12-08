from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from .models import User


class OireAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.fields.TextInput(attrs={
        'placeholder': 'e.g ****@aun.edu.ng',
        'class': 'form-control',
        'autofocus': ''
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, request=None, *args, **kwargs):
        super(OireAuthenticationForm, self).__init__(request, *args, **kwargs)
        self.fields['username'].label = "AUN Email"


class OirePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autofocus': '',
            'class': 'form-control'
        }),
    )
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class OirePasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="AUN Email", max_length=254, widget=forms.fields.EmailInput(attrs={
        'placeholder': 'e.g ****@aun.edu.ng',
        'class': 'form-control',
        'autofocus': ''
    }))


class OireSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autofocus': ''
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
    )


class UserAddForm(forms.models.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'school', 'groups')
        widgets = {
            'first_name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a first name',
                'class': 'form-control',
            }),
            'last_name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a last name',
                'class': 'form-control',
            }),
            'email': forms.fields.EmailInput(attrs={
                'placeholder': 'Enter an email',
                'class': 'form-control',
            }),
            'school': forms.fields.Select(attrs={
                'class': 'form-control'
            }),
            'groups': forms.fields.SelectMultiple(attrs={
                'class': 'form-control',
            }),

        }


class UserEditForm(forms.models.ModelForm):
    class Meta(UserAddForm.Meta):
        fields = UserAddForm.Meta.fields + ('user_permissions', 'is_active')
        widgets = UserAddForm.Meta.widgets
        widgets['user_permissions'] = forms.fields.SelectMultiple(attrs={
            'class': 'form-control',
        })
