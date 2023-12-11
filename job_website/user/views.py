from django.shortcuts import render, redirect
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Employee

def user_register(request):
    template = 'user_register.html'
    context = {
        'title' : 'User Register',
    }
    return render(request, template, context)

def add_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        auth_user = AuthUser.objects.create_user(username=email, email=email, password=password)
        auth_user.save()
        
        Employee.objects.create(
            email=email,
            password=make_password(password),
        )
        
        return redirect('user_login')
    else:
        return redirect('user_register')
    
def user_login(request):
    template = 'user_login.html'
    context = {
        'title' : 'User Login',
    }
    return render(request, template, context)


def user_toLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Employee.objects.get(email=email)
        if check_password(password, user.password):
            return redirect('homepage')
        else:
            return redirect('user_login')
    else:
        return redirect('user_login')

def homepage(request):
    template = 'user_homepage.html'
    context = {
        'title' : 'Homepage',
    }
    return render(request, template, context)
