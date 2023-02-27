from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from .models import *


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = Users
        fields = ('username','password')

class UserRestrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'registration-form__input'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'registration-form__input'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'registration-form__input'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'registration-form__input'
    }))
    class Meta:
        model = Users
        fields = ('username','email','password1','password2')