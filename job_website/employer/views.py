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


def add_employer(request):
    if request.method == 'POST':
        # Access form data directly from request.POST
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company = request.POST.get('company')
        address = request.POST.get('company_address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Create a new Job instance and save to the database
        Details.objects.create(
            first_name=first_name,
            last_name=last_name,
            company=company,
            address=address,
            email=email,
            phone=phone,
            password=password
        )

        # Redirect to a success page or do something else
        # Adjust 'success_page' to your actual success page URL
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
