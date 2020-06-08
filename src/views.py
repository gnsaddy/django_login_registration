from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'index.html')


def cal(request):
    res = None
    n1 = request.POST.get('num1')
    n2 = request.POST.get('num2')

    if request.POST.get('plus'):
        res = int(n1) + int(n2)
    if request.POST.get('minus'):
        res = int(n1) - int(n2)
    if request.POST.get('mult'):
        res = int(n1) * int(n2)
    if request.POST.get('divide'):
        try:
            res = int(n1) / int(n2)
        except ZeroDivisionError:
            res = 'DivideByZeroException'

    return render(request, 'calculator.html', {'result': res})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        pass1 = request.POST.get('password1')

        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('user_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 == pass2:
            if pass1.isnumeric():
                messages.warning(request, 'This password is entirely numeric.')
            if len(pass1) < 8:
                messages.warning(request, 'This password is too short. It must contain at least 8 characters.')
            if User.objects.filter(username=username).exists():
                print('User name taken')
                messages.warning(request, 'A user with that username already exists.')
            elif User.objects.filter(email=email).exists():
                print('Email already taken')
                messages.warning(request, 'Email address already taken')
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email,
                                                password=pass1)
                user.save()
                print('user created')
                messages.success(request, f'Account created for {username}.')
                return redirect('login')
        else:
            print('password not matched')
            messages.warning(request, 'The two password fields didn’t match.')
        return redirect('register')

    else:
        return render(request, 'registration.html')
