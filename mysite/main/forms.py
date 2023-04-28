from django import forms
from .models import RecoveryMessage
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    message = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Type your message here...'}))
    
    class Meta:
        model = RecoveryMessage
        fields = ['message']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
