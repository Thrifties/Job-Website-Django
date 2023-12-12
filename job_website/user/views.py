
from django.shortcuts import render, redirect
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Employee

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

def profile(request):
    template = 'profile.html'
    userId = request.session.get('id')
    employee = Employee.objects.get(id=userId)
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


def user_toLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Employee.objects.get(email=email)
        if check_password(password, user.password):
            request.session['id'] = user.id
            request.session['email'] = user.email
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
        'title': f'{job.title} - Job Detail', 'job': job,
    }
    return render(request, template, context)


def user_application_process(request, id):
    template = 'user_application_process.html'
    job = get_object_or_404(Job, id=id)
    employee = Employee.objects.get(email='kenshin.sayson@gmail.com')
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
        return redirect('company')  # Redirect to the company list or another page

    context = {
        'title': 'User Company Profile',
        'company': company,
    }

    return render(request, 'user_company_profile.html', context)

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
