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
                request.session['company'] = user.company
                request.session['phone'] = user.phone
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
        # hashed_password = make_password(password)

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
    user_id = request.session.get('id')
    user = Details.objects.get(id=user_id)
    context = {
        'title': 'Profile Settings Page',
        'user': user
    }
    return render(request, template, context)


def edit_profile(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company = request.POST.get('company_name')  # Correct field name
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Update user profile
        user_id = request.session.get('id')  # Get user ID from session
        try:
            # Fetch user from Details model
            user = Details.objects.get(id=user_id)
            user.first_name = first_name
            user.last_name = last_name
            user.company = company
            user.email = email
            user.phone = phone
            user.save()

            # Display success message
            messages.success(request, 'Profile updated successfully!')

            # Redirect back to the profile settings page
            return redirect('profile_settings')
        except Details.DoesNotExist:
            # Handle if the user doesn't exist
            messages.error(request, 'User does not exist!')
            return redirect('profile_settings')

    # If it's a GET request or form not valid, render the form again
    return render(request, 'profile_settings.html')


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
        company = request.POST.get('company')
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
            company=company,
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


from django.http import JsonResponse
from .models import Company

def add_company_profile(request):
    try:
        # Create a new company with default values
        new_company = Company.objects.create(
            company_name="-",
            company_email="-",
            location="-",
            website="-",
            scope="-",
            overview="-",
            join_us="-",
            profile_picture_path="-",
            cover_photo_path="-",
        )

        # Update the employerID to the same value as id
        new_company.employerID = new_company.id

        # Save the company again to update the employerID
        new_company.save()

        # Return success and company information
        company_info = {
            'company_name': new_company.company_name,
            'company_email': new_company.company_email,
            'location': new_company.location,
            'website': new_company.website,
            'scope': new_company.scope,
            'overview': new_company.overview,
            'join_us': new_company.join_us,
            'profile_picture_path': new_company.profile_picture_path,
            'cover_photo_path': new_company.cover_photo_path,
            'employerID': new_company.employerID,
        }

        return JsonResponse({'success': True, 'message': 'Company added successfully', 'company': company_info})
    except Exception as e:
        # Return failure and error message
        return JsonResponse({'success': False, 'message': str(e)})

from .models import Company

def get_company_data(request, company_id):
    try:
        # Retrieve the company data based on the provided company_id
        company = Company.objects.get(id=company_id)

        company_info = {
            'company_name': company.company_name,
            'company_email': company.company_email,
            'location': company.location,
            'website': company.website,
            'scope': company.scope,
            'overview': company.overview,
            'join_us': company.join_us,
            'profile_picture_path': company.profile_picture_path,
            'cover_photo_path': company.cover_photo_path,
        }

        return JsonResponse({'success': True, 'company': company_info})
    except Company.DoesNotExist:
        return JsonResponse({'success': False, 'message': f'Company with id={company_id} not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def update_company_profile(request, company_id):
    try:
        company = Company.objects.get(employerID=company_id)
    except Company.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Company not found'}, status=404)

    # Exclude 'employerID' from the form fields
    form = CompanyForm(request.POST, instance=company)
    if form.is_valid():
        # Set 'employerID' manually before saving the form
        form.instance.employerID = company_id
        form.save()
        return JsonResponse({'success': True, 'message': 'Company profile updated successfully'})
    else:
        # Return validation errors as part of the response
        return JsonResponse({'success': False, 'message': 'Form validation failed', 'errors': form.errors}, status=400)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company

# @csrf_exempt
# def update_profile_picture(request):
    # if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    #     try:
    #         company_id = int(request.POST.get('company_id'))
    #         company = Company.objects.get(employerID=company_id)

    #         profile_picture = request.FILES.get('profile_picture')
    #         if profile_picture:
    #             # Save the file to the desired folder
                
    #             profile_picture_path = f'employer/static/resources/profile_picture/profile_picture_{company_id}.png'
    #             profile_picture_name = f'profile_picture_{company_id}.png'
    #             with open(profile_picture_path, 'wb') as file:
    #                 for chunk in profile_picture.chunks():
    #                     file.write(chunk)

    #             # Update the profile_picture_path for the Company instance
    #             company.profile_picture_path = profile_picture_name
    #             company.save()

    #             return JsonResponse({'success': True, 'message': 'Profile picture updated successfully'})
    #         else:
    #             return JsonResponse({'success': False, 'message': 'No file provided'})
    #     except Exception as e:
    #         return JsonResponse({'success': False, 'message': str(e)})

    # return JsonResponse({'success': False, 'message': 'Invalid request'})


@csrf_exempt
def update_profile_picture(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            company_id = int(request.POST.get('company_id'))
            company = Company.objects.get(employerID=company_id)

            profile_picture = request.FILES.get('profile_picture')
            if profile_picture:
                # Determine the file extension dynamically
                file_extension = profile_picture.name.split('.')[-1]
                
                # Save the file to the desired folder
                profile_picture_path = f'employer/static/resources/profile_picture/profile_picture_{company_id}.png'
                profile_picture_name = f'profile_picture_{company_id}.png'
                
                with open(profile_picture_path, 'wb') as file:
                    for chunk in profile_picture.chunks():
                        file.write(chunk)

                # Update the profile_picture_path for the Company instance
                company.profile_picture_path = profile_picture_name
                company.save()

                return JsonResponse({'success': True, 'message': 'Profile picture updated successfully'})
            else:
                return JsonResponse({'success': False, 'message': 'No file provided'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request'})
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
    
