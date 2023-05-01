from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RecoveryMessage
from .forms import MessageForm, SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

@login_required
def home(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            recovery_message = form.save(commit=False)
            recovery_message.user = request.user
            recovery_message.save()
            form = MessageForm()
            return redirect('home')
    else:
        form = MessageForm()
    messages = RecoveryMessage.objects.all().order_by('-created_at')[:10][::-1]
    return render(request, 'main/home.html', {'form': form, 'recovery_messages': messages})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('messages')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")
