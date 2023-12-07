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
from .models import Applicant
from django.http import FileResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def to_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Details.objects.get(email=email)
        if user:
            if user.password == password:
                request.session['id'] = user.id
                request.session['email'] = user.email
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                return render(request, 'dashboard.html')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return redirect('login')

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
    
        template = 'login.html'
        context = {
            'title': 'Login Page'
        }
        return render(request, template, context)

def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return redirect('login')

def add_employer(request):
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company = request.POST.get('company')
        address = request.POST.get('company_address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        #hashed_password = make_password(password)

        Details.objects.create(
            first_name=first_name,
            last_name=last_name,
            company=company,
            address=address,
            email=email,
            phone=phone,
            password=password
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

            job_details = {
                'title': job.title,
                'number_of_people': job.number_of_people,
                'salary': job.salary,
                'category': job.category,
                'location': job.location,
                'description': job.description,
                'requirements': job.requirements,
                # Format date as string if not None
                'date': job.date.strftime('%Y-%m-%d') if job.date else None,
                'status': job.status


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
            job.requirements = updated_data.get(
                'requirements', job.requirements)
            job.date = updated_data.get('date', job.date)
            job.status = updated_data.get('status', job.status)
            print(f"Old Status: {job.status}")
            # Save the changes
            job.save()
            print(f"New Status: {job.status}")

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Invalid data.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        job.delete()
        return JsonResponse({'message': 'Job deleted successfully.'})

    return JsonResponse({'message': 'Invalid request.'}, status=400)

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


def applicant_list(request):

    applicants = Applicant.objects.all()
    template = 'manage_applicants.html'
    context = {
        'title': 'Applicants Page',
        'applicants': applicants
    }
    return render(request, template, context)


def view_resume(request, resume_filename):

    applicant = get_object_or_404(Applicant, resume=resume_filename)
    file_path = applicant.resume.path
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


@require_POST
def approve_applicant(request, applicant_id):
    applicant = get_object_or_404(Applicant, id=applicant_id)
    # Perform approval logic here
    applicant.status = 'Approved'
    applicant.save()
    return JsonResponse({'status': 'success'})


@csrf_exempt
def reject_applicant(request, applicant_id):
    applicant = get_object_or_404(Applicant, id=applicant_id)
    rejection_reason = request.POST.get('rejection_reason', '')
    if request.method == 'POST':
        applicant.status = 'Rejected'
        applicant.rejection_reason = rejection_reason
        applicant.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
