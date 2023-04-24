from django.shortcuts import render, redirect
from .models import MyUser, ChatMessage
from .forms import MyUserForm
# Create your views here.

login_user = ''

def home(request):
    messages = ChatMessage.objects.all().order_by('created')
    return render(request, 'main/home.html', context={
        'login_user': login_user,
        'messages': messages
    })

def register(request):
    chars = '!@#$%^&*()'
    char_count = 0
    number_count = 0
    let_count = 0
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        my_name = request.POST.get('user_name')
        my_pass = request.POST.get('user_password')
        if len(my_pass) < 8:
            return redirect('register')
        else:
            for i in my_pass:
                if i.isdigit():
                    number_count += 1
                elif i in chars:
                    char_count += 1
                else:
                    let_count += 1
            if number_count >= 1 and char_count >= 1 and let_count >= 6:
                MyUser.objects.create(user_name=my_name, user_password=my_pass)
                return redirect('login')
            else:
                return redirect('register')
    else:
        form = MyUserForm()
    return render(request, 'main/signup.html', context={
        'form':form
    })


def login(request):
    global login_user
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        name = request.POST.get('user_name')
        password = request.POST.get('user_password')
        obj = MyUser.objects.all()
        for i in obj:
            if name == i.user_name and password == i.user_password:
                login_user = name
                return redirect('home')
        else:
            return redirect('login')
    else:
        form = MyUserForm()

    return render(request, 'main/login.html', context={
        'form':form,
        'login_user':login_user
    })


def logout(request):
    global login_user
    login_user = ''
    return redirect('home')

def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            ChatMessage.objects.create(user=request.user, message=message)
    return redirect('home')

def chat_messages(request):
    messages = ChatMessage.objects.all()
    context = {'messages': messages}
    return render(request, 'chat.html', context)