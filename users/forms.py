from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CreatePost, UsersProfile

class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class UsersProfile(forms.ModelForm):
    class Meta:
        model = UsersProfile
        fields = ['sec_name', 'email', 'description', 'profile_pic', 'phone_number', 'gender', 'age']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreatePost(forms.ModelForm):
    class Meta:
        # if this model = CreatePost not working try models.CreatePost
        model = CreatePost
        fields = ['picture', 'title', 'description']
