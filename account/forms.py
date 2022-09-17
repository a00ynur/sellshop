from dataclasses import field
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


USER = get_user_model()

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Re-enter the password here'
            }))

    class Meta:
        model = USER
        fields = (
            'gender',
            'username',
            "first_name",
            "last_name",
            'email',
            'birthday',
            'number',
            'password',
            "confirm_password",
        )

        widgets = {
            'gender': forms.Select(attrs={
                'placeholder':'Women or Men', 
                'class': 'form-control', 
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username here'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name here'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name here'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
            'birthday': forms.DateInput(attrs={
                'placeholder':'Birthday here', 
                'class': 'form-control',
                'type': 'date',                                                                 
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number here'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password here'
            }),
            
           
        }
    def clean(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError("Make sure your password is the same.")
        return super().clean()


class LoginForm(AuthenticationForm):
    class Meta:
        model = USER
        fields = (
            'username',
            'password',
        )
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username here'})), 
        
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password here'
    }))


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }), max_length=255)


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
                                    widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'New Password'
            }))
    new_password2 = forms.CharField(
                                    widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm New Password'
            }))


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old password"),
                                   widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Old Password'
                                    }))
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                'placeholder': 'New Password'}))
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                'placeholder': 'Confirm Password'}))


class UpdatePersonalInfoForm(forms.ModelForm):
    class Meta:
        model = USER
        fields = (
            "first_name",
            "last_name",
            'email',
            'birthday',
            'gender',
        )
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name here'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name here'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address here'
            }),
            'birthday': forms.DateInput(attrs={
                'placeholder':'Birthday here', 
                'class': 'form-control',
                'type': 'date',                                                                 
            }),
            'gender': forms.Select(attrs={
                'placeholder':'Men or Women', 
                'class': 'form-control', 
            }),
        }