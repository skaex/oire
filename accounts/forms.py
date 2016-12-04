from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation


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
        label=("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autofocus': '',
            'class': 'form-control'
        }),
    )
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class OirePasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=("AUN Email"), max_length=254, widget=forms.fields.EmailInput(attrs={
        'placeholder': 'e.g ****@aun.edu.ng',
        'class': 'form-control',
        'autofocus': ''
    }))

class OireSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autofocus': ''
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
    )
