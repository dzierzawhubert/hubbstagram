from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsersProfile(forms.ModelForm):
    class Meta:
        model = models.UsersProfile
        fields = ['name', 'sec_name', 'email', 'phone_number', 'gender', 'age']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
