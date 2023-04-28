from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import RecoveryMessage
from .forms import MessageForm, SignupForm
from django.contrib.auth.forms import AuthenticationForm


from django.shortcuts import render

@login_required
def home(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            recovery_message = form.save(commit=False)
            recovery_message.user = request.user
            recovery_message.save()
    else:
        form = MessageForm()
    
    messages = RecoveryMessage.objects.filter(user=request.user)
    return render(request, 'main/home.html', {'form': form, 'recovery_messages': messages})

@login_required
def recover_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            recovery_message = form.save(commit=False)
            recovery_message.user = request.user
            recovery_message.save()
            messages = RecoveryMessage.objects.filter(user=request.user)
            return render(request, 'home.html', {'recovery_messages': messages})
    else:
        messages = RecoveryMessage.objects.filter(user=request.user)
        return render(request, 'home.html', {'recovery_messages': messages})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})