from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUser

class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['user_name', 'user_password']
