from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Job, JobStatus
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Job, Details
from .forms import CompanyForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
# Create your views here.


def dashboard(request):

    template = 'dashboard.html'
    context = {
        'title': 'Dashboard Page'
    }
    return render(request, template, context)


def register(request):

    template = 'register.html'
    context = {
        'title': 'Register Page'
    }
    return render(request, template, context)


def login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        first_name = request.POST.get('first_name')

        # Authenticate user
        employer_phone = Details.objects.filter(phone=phone).first()
        employer_name = Details.objects.filter(first_name=first_name).first()

        if employer_phone is not None and employer_name is not None:
            user = authenticate(
                request, phone=employer_phone, first_name=employer_name)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard.html')
            else:
                messages.error(
                    request, 'Invalid phone number or first name.')
        
    context = {
        'title': 'Login Page'
    }
    
    return render(request, 'login.html', context)

def add_employer(request):
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company = request.POST.get('company')
        address = request.POST.get('company_address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        hashed_password = make_password(password)

        Details.objects.create(
            first_name=first_name,
            last_name=last_name,
            company=company,
            address=address,
            email=email,
            phone=phone,
            password=hashed_password
        )

        return redirect('register')

    context = {
        'title': 'Register Page',
    }

    return render(request, 'register.html', context)


def profile_settings(request):

    template = 'profile_settings.html'
    context = {
        'title': 'Profile Settings Page'
    }
    return render(request, template, context)


def post_job(request):
    jobs = Job.objects.all()  # Retrieve all Job objects from the database

    if request.method == 'POST':
        # Your existing code for adding a new job

        context = {
            'title': 'Post Job Page',
            'jobs': jobs,
        }

        return render(request, 'post_job.html', context)

    context = {
        'title': 'Post Job Page',
        'jobs': jobs,
    }

    return render(request, 'post_job.html', context)


def add_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        number_of_people = request.POST.get('number_of_people')
        salary = request.POST.get('salary')
        category = request.POST.get('category')
        location = request.POST.get('location')
        description = request.POST.get('description')
        date = request.POST.get('date')
        requirements = request.POST.get('requirements')
        status = request.POST.get('status')

        # Create a new Job instance and save to the database
        Job.objects.create(
            title=title,
            number_of_people=number_of_people,
            salary=salary,
            category=category,
            location=location,
            description=description,
            date=date,
            requirements=requirements,
            status=status
        )

        # Redirect to a success page or do something else
        # Adjust 'success_page' to your actual success page URL
        return redirect('post_job')

    context = {
        'title': 'Post Job Page',
    }

    return render(request, 'post_job.html', context)


def job_list(request):
    jobs = Job.objects.all()  # Retrieve all Job objects from the database
    print(jobs)  # Add this line for debugging
    context = {
        'title': 'Job List Page',
        'jobs': jobs,  # Pass the retrieved jobs to the template
    }

    return render(request, 'post_job.html', context)


def get_job_details(request):
    if request.method == 'GET':
        job_id = request.GET.get('job_id', None)

        if job_id is not None:
            job = get_object_or_404(Job, id=job_id)

            # Assuming Job has fields like title, number_of_people, salary, etc.
            job_details = {
                'title': job.title,
                'number_of_people': job.number_of_people,
                'salary': job.salary,
                'category': job.category,
                'location': job.location,
                'description': job.description,
                # Format date as string if not None
                'date': job.date.strftime('%Y-%m-%d') if job.date else None,
                # 'requirement1': job.requirement1,
                # 'requirement2': job.requirement2,
                # 'requirement3': job.requirement3,
            }

            return JsonResponse(job_details)
        else:
            return JsonResponse({'error': 'Job ID not provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


@require_POST
@csrf_exempt  # Use this decorator for simplicity, but consider using a more secure method for production
def save_job_changes(request):
    try:
        job_id = request.POST.get('job_id', None)
        updated_data_json = request.POST.get('updated_data', None)

        if job_id is not None and updated_data_json is not None:
            updated_data = json.loads(updated_data_json)
            job = Job.objects.get(id=job_id)

            # Update job fields with new data
            job.title = updated_data.get('title', job.title)
            job.number_of_people = updated_data.get(
                'number_of_people', job.number_of_people)
            job.salary = updated_data.get('salary', job.salary)
            job.category = updated_data.get('category', job.category)
            job.location = updated_data.get('location', job.location)
            job.description = updated_data.get('description', job.description)
            job.date = updated_data.get('date', job.date)
            # job.requirement1 = updated_data.get(
            #     'requirement1', job.requirement1)
            # job.requirement2 = updated_data.get(
            #     'requirement2', job.requirement2)
            # job.requirement3 = updated_data.get(
            #     'requirement3', job.requirement3)

            # Save the changes
            job.save()

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Invalid data.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def company_profile(request):

    template = 'company_profile.html'
    context = {
        'title': 'Company Profile Page'
    }
    return render(request, template, context)


def add_company_profile(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company profile saved successfully.')
            return redirect('company_profile')
        else:
            messages.error(
                request, 'Form submission has errors. Please check the form.')
    else:
        form = CompanyForm()

    context = {
        'title': 'Add Company Profile',
        'form': form,
    }

    return render(request, 'company_profile.html', context)
