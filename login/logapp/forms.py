from django import forms
from logapp.models import Login,Register
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email','password']
        labels={
            'email':_('Email'),
            'password':_("Password"),
        }

        widgets={
            'password':forms.PasswordInput(),
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['firstName','lastName','email','pass1','pass2']
        labels={
            'firstName':_('First Name'),
            'lastName':_('Last Name'),
            'email':_('Email'),
            'pass1':_('Password'),
            'pass2':_('Confirm Password')
        }
        widgets={
            'pass1':forms.PasswordInput(),
            'pass2':forms.PasswordInput(),
        }