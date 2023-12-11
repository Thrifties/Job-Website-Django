
from django.shortcuts import render, redirect
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Employee
from django.shortcuts import render, get_object_or_404
from employer.models import Job
from django.views import View
from django.db.models import Q
# Create your views here.


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


def homepage(request):
    # Fetch all jobs from the Job model
    jobs = Job.objects.all()

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        jobs = jobs.filter(Q(title__icontains=search_query))
    context = {
        'title': 'Homepage',
        'jobs': jobs,
    }


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
    
def user_toLogout(request):
    template = 'user_login.html'
    return render(request, template)

def job_detail(request, job_id):
    # Retrieve the job details using the job_id
    template = 'job_detail.html'
    job = get_object_or_404(Job, id=job_id)
    context = { 
        'title': f'{job.title} - Job Detail','job': job,
    }
    return render(request, template, context)

def user_application_process(request):
    template = 'user_application_process.html'
    context = {
        'title' : 'User Application Process',
    }
    return render(request, template, context)

