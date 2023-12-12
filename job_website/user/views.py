
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Employee, GraduateTracer
from .forms import GraduateTracerForm
from django.views.decorators.http import require_POST

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
def graduate_tracer(request):
    template = 'graduate_tracer.html'

    if request.method == 'POST':
        form = GraduateTracerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('graduate_tracer')  # Replace 'success_page' with your success page URL
    else:
        form = GraduateTracerForm()

    context = {
        'title': 'Graduate Tracer Form',
        'form': form,
        'years': range(2010, 2024),
        'civil_status': ['Single', 'Married', 'Divorced', 'Widowed'],
        'sexes' : ['Male', 'Female'],
        'scholarship_recipient': ['Yes, I am recipient of Government scholarship program', 
                         'Yes, I am recipient of private scholarship program', 
                         'No, I am not recipient of any scholarship program'],
        'employed_by': ['Yes with employer', 'Yes self-employed', 'No'],
        'organization_types': ['Public/Government', 'NGO', 'Non-profit', 'Private Owned'],
        'employment_status': ['Regular/Permanent', 'Temporary', 
                              'Casual', 'Contractual', 'Self-employed'],
        'education_attained': ['Certificate in Two Year Course','College graduate','With Units in Masters Degree',
                               'Masters Degree Holder','With Units in Doctoral Degree','Doctoral Degree Holder',],
        'work_location': ['Local', 'Abroad'],
        'line_of_business': [ 'BPO','Trade/Industry','Legal',
                             'Telecom/Communications',
                             'IT/Computer/Software','Banking and Finance',
                             'Insurance','Services','Government','Academic',
                             'Manufacturing','Other'],
        'gross_monthly_rate': ['Below P 10,000','P 10,000 to P 20,000','P 21,000 to P 30,000',
                                'P 31,000 to P 40,000','P 41,000 to P 50,000',
                                'P 51,000 to P 60,000','P 61,000 to P 70,000','Above P 71,000'],
        'course_related_to_job': ['Yes', 'No'],
        'first_job_found_duration': ['Less than a month', '1-3 months', '3-6 months', '6-12 months', 'Above 1 year', 'Above 3 years'],
        'first_job_present': ['Yes', 'No'],
        'first_job_stay_duration': ['Less than a month', '1-3 months', '3-6 months', '6-12 months', 'Above 1 year', 'Above 3 years'],
        'known_first_job_through': [ 'Responded to job advertisement','Arranged by school','Walk-In Applicant','Family Business',
                                   'Recommended by Someone','Information from Friends','Others'],
        'first_job_level_position': ['Rank or Clerical','Professional,Techinical,Supervisory','Managerial or Executive', 'Self-employed'],
        'gross_monthly_earning_first_job':  ['Below P 10,000','P 10,000 to P 20,000','P 21,000 to P 30,000',
                                'P 31,000 to P 40,000','P 41,000 to P 50,000',
                                'P 51,000 to P 60,000','P 61,000 to P 70,000','Above P 71,000'],
        'curriculum_related_to_first_job': ['Yes', 'No'],
        'rates': [1, 2, 3, 4],
}

    return render(request, template, context)

@require_POST
def add_tracer(request):
    college = request.POST.get('college')
    course = request.POST.get('course')
    name = request.POST.get('name')
    year_graduated = request.POST.get('year_graduated')
    address = request.POST.get('address')
    civil_status = request.POST.get('civil_status')
    age = request.POST.get('age')
    email = request.POST.get('email')
    contact_number = request.POST.get('contact_number')
    sex = request.POST.get('sex')
    education_attained = request.POST.get('education_attained')
    scholarship_recipient = request.POST.get('scholarship_recipient')
    presently_employed = request.POST.get('presently_employed')
    organization_or_employer = request.POST.get('organization_or_employer')
    organization_type = request.POST.get('organization_type')
    employment_status = request.POST.get('employment_status')
    work_location = request.POST.get('work_location')
    current_occupation = request.POST.get('current_occupation')
    years_in_company = request.POST.get('years_in_company')
    major_line_of_business = request.POST.get('major_line_of_business')
    reason_to_stay = request.POST.get('reason_to_stay')
    gross_monthly_rate = request.POST.get('gross_monthly_rate')
    award = request.POST.get('award')
    key_position = request.POST.get('key_position')
    course_related_to_job = request.POST.get('course_related_to_job')
    first_job_found_duration = request.POST.get('first_job_found_duration')
    first_job_present = request.POST.get('first_job_present')
    first_job_stay_duration = request.POST.get('first_job_stay_duration')
    known_first_job_through = request.POST.get('known_first_job_through')
    first_job_level_position = request.POST.get('first_job_level_position')
    gross_monthly_earning_first_job = request.POST.get('gross_monthly_earning_first_job')
    curriculum_related_to_first_job = request.POST.get('curriculum_related_to_first_job')
    communication_skills = request.POST.get('communication_skills')
    human_relations_skills = request.POST.get('human_relations_skills')
    entrepreneurial_skills = request.POST.get('entrepreneurial_skills')
    information_technology_skills = request.POST.get('information_technology_skills')
    problem_solving_skills = request.POST.get('problem_solving_skills')
    critical_thinking_skills = request.POST.get('critical_thinking_skills')
    
    GraduateTracer.objects.create(
        college=college,
        course=course,
        name=name,
        year_graduated=year_graduated,
        address=address,
        civil_status=civil_status,
        age=age,
        email=email,
        contact_number=contact_number,
        sex=sex,
        education_attained=education_attained,
        scholarship_recipient=scholarship_recipient,
        presently_employed=presently_employed,
        organization_or_employer=organization_or_employer,
        organization_type=organization_type,
        employment_status=employment_status,
        work_location=work_location,
        current_occupation=current_occupation,
        years_in_company=years_in_company,
        major_line_of_business=major_line_of_business,
        reason_to_stay=reason_to_stay,
        gross_monthly_rate=gross_monthly_rate,
        award=award,
        key_position=key_position,
        course_related_to_job=course_related_to_job,
        first_job_found_duration=first_job_found_duration,
        first_job_present=first_job_present,
        first_job_stay_duration=first_job_stay_duration,
        known_first_job_through=known_first_job_through,
        first_job_level_position=first_job_level_position,
        gross_monthly_earning_first_job=gross_monthly_earning_first_job,
        curriculum_related_to_first_job=curriculum_related_to_first_job,
        communication_skills=communication_skills,
        human_relations_skills=human_relations_skills,
        entrepreneurial_skills=entrepreneurial_skills,
        information_technology_skills=information_technology_skills,
        problem_solving_skills=problem_solving_skills,
        critical_thinking_skills=critical_thinking_skills,
    )
    
    return redirect('graduate_tracer')  # Replace 'success_page' with your success page URL