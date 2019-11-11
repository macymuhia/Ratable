from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User

from .models import *


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]
