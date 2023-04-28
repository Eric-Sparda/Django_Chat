from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RecoveryMessage
from .forms import MessageForm, SignupForm

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