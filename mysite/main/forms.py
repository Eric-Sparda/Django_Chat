from django import forms
from .models import RecoveryMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your message here...'}))

    class Meta:
        model = RecoveryMessage
        fields = ['message']

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
