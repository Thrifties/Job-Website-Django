
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
            request.session['id'] = user.id
            request.session['email'] = email
            return redirect('profile')
        else:
            # Handle case where password is incorrect
            return redirect('user_login')
    else:
        return redirect('user_login')


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

def profile(request):
    template = 'profile.html'
    email = request.session.get('email')
    employee = Employee.objects.get(email=email)
    context = {
        'title': 'Profile',
        'employee': employee,
    }
    return render(request, template, context)

def company_profile(request, id):
    # Your view logic here...
    # Retrieve the company details using the 'id' parameter

    context = {
        'title': 'Company Profile',
        # Other context variables...
    }

    return render(request, 'company_profile.html', context)

from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
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
            profile_picture_path='',  # Blank value for location_of_residence
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
      
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404


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


def user_my_jobs(request):
    # Fetch all applicants from the Applicant model
    applicants = Applicant.objects.filter(email=request.session.get('email'))
    # Create a list of tuples where each tuple contains an Applicant object and the corresponding Job object
    applicant_jobs = [(applicant, Job.objects.get(title=applicant.job))
                      for applicant in applicants]
    template = 'user_my_jobs.html'
from django.http import JsonResponse

def get_employee_data(request, employee_id):
    try:
        # Retrieve the employee data based on the provided employee_id
        employee = Employee.objects.get(id=employee_id)

        employee_info = {
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'middle_name': employee.middle_name,
            'birthdate': employee.birthdate,
            'civil_status': employee.civil_status,
            'email': employee.email,
            'contact_number': employee.contact_number,
            'permanent_address': employee.permanent_address,
            'region_of_origin': employee.region_of_origin,
            'province': employee.province,
            'location_of_residence': employee.location_of_residence,
            'password': employee.password,
            'profile_picture_path': employee.profile_picture_path,
        }

        return JsonResponse({'success': True, 'employee': employee_info})
    except Employee.DoesNotExist:
        return JsonResponse({'success': False, 'message': f'Employee with id={employee_id} not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    
    
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class UpdateEmployeeProfile(View):
    def post(self, request, employee_id):
        # Retrieve the employee instance or return a 404 response if not found
        employee = get_object_or_404(Employee, id=employee_id)

        # Update employee profile fields based on the posted data
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.middle_name = request.POST.get('middle_name')
        employee.email = request.POST.get('email')
        employee.contact_number = request.POST.get('contact_number')
        employee.civil_status = request.POST.get('civil_status')
        employee.birthdate = request.POST.get('birthdate')
        employee.permanent_address = request.POST.get('permanent_address')
        employee.province = request.POST.get('province')
        employee.region_of_origin = request.POST.get('region_of_origin')
        employee.location_of_residence = request.POST.get('location_of_residence')

        # Save the updated employee instance
        employee.save()

        return JsonResponse({'success': True, 'message': 'Employee profile updated successfully'})

from django.views.decorators.http import require_POST
from .models import EducationalBackground

@csrf_exempt  # Use csrf_exempt for simplicity, consider using a csrf token for production
@require_POST
def add_educational_background(request):
    try:
        # Extract data from AJAX request
        degree = request.POST.get('degree')
        college_or_university = request.POST.get('college_or_university')
        year_graduated = request.POST.get('year_graduated')
        honors_or_awards = request.POST.get('honors_or_awards')
        employee_id = request.POST.get('employee_id')

        # Create a new EducationalBackground instance
        educational_background = EducationalBackground(
            degree=degree,
            college_or_university=college_or_university,
            year_graduated=year_graduated,
            honors_or_awards=honors_or_awards,
            employee_id=employee_id
        )

        # Save the instance to the database
        educational_background.save()

        # Return a success response
        return JsonResponse({'success': True, 'message': 'Educational background added successfully'})
    except Exception as e:
        # Return an error response
        return JsonResponse({'success': False, 'message': str(e)})


def fetch_educational_background(request):
    employee_id = request.GET.get('employee_id')
    try:
        educational_data = EducationalBackground.objects.filter(employee_id=employee_id).values()
        return JsonResponse({'success': True, 'message': 'Educational background fetched successfully', 'data': list(educational_data)})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    
    

from .models import CareerHistory

@csrf_exempt  # Use csrf_exempt for simplicity, consider using a csrf token for production
@require_POST
def add_career_history(request):
    try:
        # Extract data from AJAX request
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        started = request.POST.get('started')
        ended = request.POST.get('ended')
        description = request.POST.get('description')
        employee_id = request.POST.get('employee_id')

        # Create a new CareerHistory instance
        career_history = CareerHistory(
            job_title=job_title,
            company_name=company_name,
            started=started,
            ended=ended,
            description=description,
            employee_id=employee_id
        )

        # Save the instance to the database
        career_history.save()

        # Return a success response
        return JsonResponse({'success': True, 'message': 'Career history added successfully'})
    except Exception as e:
        # Return an error response
        return JsonResponse({'success': False, 'message': str(e)})

from .models import CareerHistory

def fetch_career_history(request):
    employee_id = request.GET.get('employee_id')
    try:
        career_data = CareerHistory.objects.filter(employee_id=employee_id).values()
        return JsonResponse({'success': True, 'message': 'Career history fetched successfully', 'data': list(career_data)})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    

from .models import AdvanceStudies

@csrf_exempt
@require_POST
def add_advance_studies(request):
    try:
        # Extract data from AJAX request
        training_title = request.POST.get('training_title')
        training_institution = request.POST.get('training_institution')
        duration = request.POST.get('duration')
        credits_earned = request.POST.get('credits_earned')
        employee_id = request.POST.get('employee_id')

        # Create a new AdvanceStudies instance
        advance_studies = AdvanceStudies(
            training_title=training_title,
            training_institution=training_institution,
            duration=duration,
            credits_earned=credits_earned,
            employee_id=employee_id
        )

        # Save the instance to the database
        advance_studies.save()

        # Return a success response
        return JsonResponse({'success': True, 'message': 'Advance studies added successfully'})
    except Exception as e:
        # Return an error response
        return JsonResponse({'success': False, 'message': str(e)})



def fetch_advance_studies(request):
    employee_id = request.GET.get('employee_id')
    try:
        advance_studies_data = AdvanceStudies.objects.filter(employee_id=employee_id).values()
        return JsonResponse({'success': True, 'message': 'Advance studies fetched successfully', 'data': list(advance_studies_data)})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

from .models import AdvanceReason

@csrf_exempt
@require_POST
def add_advance_reason(request):
    try:
        # Extract data from AJAX request
        training_reason = request.POST.get('training_reason')
        employee_id = request.POST.get('employee_id')

        # Create a new AdvanceReason instance
        advance_reason = AdvanceReason(
            training_reason=training_reason,
            employee_id=employee_id
        )

        # Save the instance to the database
        advance_reason.save()

        # Return a success response
        return JsonResponse({'success': True, 'message': 'Advance reason added successfully'})
    except Exception as e:
        # Return an error response
        return JsonResponse({'success': False, 'message': str(e)})


def fetch_advance_reasons(request):
    employee_id = request.GET.get('employee_id')
    try:
        advance_reasons_data = AdvanceReason.objects.filter(employee_id=employee_id).values()
        return JsonResponse({'success': True, 'message': 'Advance reasons fetched successfully', 'data': list(advance_reasons_data)})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    
from .models import Skill

@csrf_exempt
@require_POST
def add_skill(request):
    try:
        # Extract data from AJAX request
        skill_name = request.POST.get('skill')
        employee_id = request.POST.get('employee_id')

        # Create a new Skill instance
        skill = Skill(skill_name=skill_name, employee_id=employee_id)

        # Save the instance to the database
        skill.save()

        # Return a success response
        return JsonResponse({'success': True, 'message': 'Skill added successfully'})
    except Exception as e:
        # Return an error response
        return JsonResponse({'success': False, 'message': str(e)})
    
def fetch_skills(request):
    employee_id = request.GET.get('employee_id')
    try:
        # Fetch skills based on the employee_id
        skills_data = Skill.objects.filter(employee_id=employee_id).values()
        return JsonResponse({'success': True, 'message': 'Skills fetched successfully', 'data': list(skills_data)})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    
from .models import ProfessionalExamination

@csrf_exempt
@require_POST
def add_professional_examination(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        exam_title = request.POST.get('exam_title')
        exam_date = request.POST.get('exam_date')
        exam_rating = request.POST.get('exam_rating')

        try:
            ProfessionalExamination.objects.create(
                employee_id=employee_id,
                exam_title=exam_title,
                exam_date=exam_date,
                exam_rating=exam_rating
            )
            return JsonResponse({'success': True, 'message': 'Professional examination added successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def fetch_professional_examinations(request):
    employee_id = request.GET.get('employee_id')
    try:
        examination_data = ProfessionalExamination.objects.filter(employee_id=employee_id).values()
        return JsonResponse({'success': True, 'message': 'Professional examinations fetched successfully', 'data': list(examination_data)})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

from .models import EducationalBackground

@csrf_exempt
@require_POST
def delete_educational_background(request):
    educational_id = request.POST.get('educational_id')

    try:
        # Assuming EducationalBackground model has a primary key named 'id'
        educational_background = get_object_or_404(EducationalBackground, id=educational_id)

        # Perform the delete operation
        educational_background.delete()

        return JsonResponse({'success': True, 'message': 'Educational background deleted successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

# views.py

from .models import CareerHistory

@csrf_exempt
@require_POST
def delete_career_history(request):
    if request.method == 'POST':
        career_history_id = request.POST.get('career_history_id')
        try:
            # Delete the career history entry
            CareerHistory.objects.filter(id=career_history_id).delete()
            return JsonResponse({'success': True, 'message': 'Career history deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

@csrf_exempt
@require_POST
def delete_advance_studies(request):
    training_id = request.POST.get('training_id')

    try:
        training = AdvanceStudies.objects.get(id=training_id)
        training.delete()
        return JsonResponse({'success': True, 'message': 'Training deleted successfully'})
    except AdvanceStudies.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Training not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    
@csrf_exempt
@require_POST
def delete_advance_reason(request):
    reason_id = request.POST.get('reason_id')

    try:
        reason = AdvanceReason.objects.get(id=reason_id)
        reason.delete()
        return JsonResponse({'success': True, 'message': 'Advance Study Reason deleted successfully'})
    except AdvanceReason.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Advance Study Reason not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt
@require_POST
def delete_skill(request):
    skill_id = request.POST.get('skill_id')

    try:
        skill = Skill.objects.get(id=skill_id)
        skill.delete()
        return JsonResponse({'success': True, 'message': 'Skill deleted successfully'})
    except Skill.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Skill not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt
@require_POST
def delete_professional_examination(request):
    examination_id = request.POST.get('examination_id')

    try:
        examination = ProfessionalExamination.objects.get(id=examination_id)
        examination.delete()
        return JsonResponse({'success': True, 'message': 'Professional examination deleted successfully'})
    except ProfessionalExamination.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Professional examination not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    
from .models import Employee

@csrf_exempt
def update_profile_picture(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            employee_id = int(request.POST.get('employee_id'))
            employee = Employee.objects.get(id=employee_id)

            profile_picture = request.FILES.get('profile_picture')
            if profile_picture:
                # Determine the file extension dynamically
                file_extension = profile_picture.name.split('.')[-1]

                # Save the file to the desired folder
                profile_picture_path = f'user/static/resources/profile_picture_user/profile_picture_{employee_id}.{file_extension}'
                profile_picture_name = f'profile_picture_{employee_id}.{file_extension}'

                with open(profile_picture_path, 'wb') as file:
                    for chunk in profile_picture.chunks():
                        file.write(chunk)

                # Update the profile_picture_path for the Employee instance
                employee.profile_picture_path = profile_picture_name
                employee.save()

                return JsonResponse({'success': True, 'message': 'Profile picture updated successfully'})
            else:
                return JsonResponse({'success': False, 'message': 'No file provided'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request'})


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
        'applicant_jobs': applicant_jobs,
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