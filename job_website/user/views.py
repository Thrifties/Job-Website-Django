
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Employee
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render, get_object_or_404
from employer.models import Job
from employer.models import Company, Applicant
from user.models import Employee
from django.views import View
from django.db.models import Q
# Create your views here.


def user_register(request):
    template = 'user_register.html'
    context = {
        'title': 'User Register',
    }
    return render(request, template, context)


def company(request):
    # Fetch all companies from the Company model
    companies = Company.objects.all()

    # Pass the list of companies to the template
    context = {
        'title': 'Company',
        'companies': companies,
    }

    # Render the template with the provided context
    return render(request, 'company.html', context)


def company_profile(request, id):
    # Your view logic here...
    # Retrieve the company details using the 'id' parameter

    context = {
        'title': 'Company Profile',
        # Other context variables...
    }

    return render(request, 'company_profile.html', context)

# def add_user(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         auth_user = AuthUser.objects.create_user(
#             username=email, email=email, password=password)
#         auth_user.save()

#         Employee.objects.create(
#             email=email,
#             password=make_password(password),
#         )

#         return redirect('user_login')
#     else:
#         return redirect('user_register')


def add_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Creating an AuthUser instance
        auth_user = AuthUser.objects.create_user(
            username=email, email=email, password=password)
        auth_user.save()

        # Creating an Employee instance with default values
        Employee.objects.create(
            email=email,
            password=make_password(password),
            first_name='user',  # Default value for first_name
            middle_name='',      # Blank value for middle_name
            birthdate=None,      # Blank value for birthdate
            civil_status='',     # Blank value for civil_status
            contact_number='',   # Blank value for contact_number
            permanent_address='',  # Blank value for permanent_address
            region_of_origin='',   # Blank value for region_of_origin
            province='',           # Blank value for province
            location_of_residence='',  # Blank value for location_of_residence
        )

        return redirect('user_login')
    else:
        return redirect('user_register')


def user_login(request):
    template = 'user_login.html'
    context = {
        'title': 'User Login',
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
    # Render the template with the provided context
    return render(request, 'user_homepage.html', context)


def user_toLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Employee.objects.get(email=email)
        except ObjectDoesNotExist:
            # Handle case where user does not exist
            return redirect('user_login')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            request.session['email'] = email
            return redirect('homepage')
        else:
            # Handle case where password is incorrect
            return redirect('user_login')
    else:
        return redirect('user_login')


def user_toLogout(request):
    logout(request)
    template = 'user_login.html'
    return render(request, template)


def job_detail(request, job_id):
    # Retrieve the job details using the job_id
    template = 'job_detail.html'
    job = get_object_or_404(Job, id=job_id)
    context = {
        'title': f'{job.title} - Job Detail', 'job': job,
    }
    return render(request, template, context)


def user_application_process(request, id):
    template = 'user_application_process.html'
    email = request.session.get('email')

    if not email:
        return redirect('user_login')

    job = get_object_or_404(Job, id=id)

    try:
        employee = Employee.objects.get(email=email)
    except ObjectDoesNotExist:
        # Handle case where employee does not exist
        return redirect('user_login')

    context = {
        'title': f'Apply for {job.title}',
        'job': job,
        'employee': employee,
    }
    return render(request, template, context)


def user_apply_job(request):
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        job_company = request.POST.get('job_company')
        employee_name = request.POST.get('employee_name')
        employee_email = request.POST.get('employee_email')
        employee_phone = request.POST.get('employee_phone_number')
        employee_address = request.POST.get('employee_address')
        employee_cv = request.FILES.get('cvUpload')

        Applicant.objects.create(
            job=job_title,
            company=job_company,
            name=employee_name,
            email=employee_email,
            phone=employee_phone,
            address=employee_address,
            resume=employee_cv,
        )

        return redirect('homepage')
    else:
        return redirect('homepage')


def user_company_profile(request, id):
    try:
        company = get_object_or_404(Company, id=id)
    except Http404:
        # Handle the case where no matching company is found
        # Redirect to the company list or another page
        return redirect('company')

    context = {
        'title': 'User Company Profile',
        'company': company,
    }

    return render(request, 'user_company_profile.html', context)

def userMyJobs(request):
    # Fetch all jobs from the Job model
    myJobs = Applicant.objects.get(email=request.session.get('email'))
    template = 'user_application_process.html'
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        myJobs = myJobs.filter(Q(title__icontains=search_query))
    context = {
        'title': 'My Jobs',
        'myJobs': myJobs,
    }
    # Render the template with the provided context
    return render(request, template, context)