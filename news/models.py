from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='логин', widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'логин'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(
        attrs={'class': 'form-input', 'placeholder': 'электронная почта'}))
    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'пароль'}))
    password2 = forms.CharField(label='повтор пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input',
                                           'placeholder': 'повтор пароля'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='логин', widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'логин'}))
    password = forms.CharField(label='пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'пароль'}))