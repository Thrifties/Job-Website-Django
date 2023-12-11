from django.http import JsonResponse
from employer.models import Details
from django.views import View
from django.shortcuts import render, redirect
from employer.models import Job
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def dashboard_admin(request):
    template = 'dashboard_admin.html'
    context = {
        'title': 'Admin Dashboard'
    }
    return render(request, template, context)


def manage_account(request):

    template = 'manage_account.html'
    context = {
        'title': 'Manage Account'
    }
    return render(request, template, context)


def admin_list_of_jobs(request):
    template = 'admin_list_of_jobs.html'

    # Retrieve all jobs from the Job model
    jobs = Job.objects.all()

    # Pass the jobs to the template context
    context = {'jobs': jobs}

    return render(request, template, context)


def approve_job(request, job_id):
    # Fetch the job instance based on the job_id
    job = Job.objects.get(pk=job_id)

    # Update the status to 'Approved'
    job.status = 'Open'
    job.save()

    # Redirect back to the job list page
    return redirect('admin_list_of_jobs')


def reject_job(request, job_id):
    # Fetch the job instance based on the job_id
    job = Job.objects.get(pk=job_id)

    # Update the status to 'Approved'
    job.status = 'Rejected'
    job.save()

    # Redirect back to the job list page
    return redirect('admin_list_of_jobs')


def delete_job(request, job_id):
    # Fetch the job instance based on the job_id
    job = Job.objects.get(pk=job_id)

    # Delete the job
    job.delete()

    # Redirect back to the rejected jobs page
    return redirect('admin_list_of_jobs')


def index(request):
    template = 'index.html'
    return render(request, template)


class GetEmployerDataView(View):
    def get(self, request, *args, **kwargs):
        try:
            # Fetch data from the Details model
            employer_data = Details.objects.all().values()

            # Convert the QuerySet to a list for serialization
            employer_data_list = list(employer_data)

            # Return the data as JSON
            return JsonResponse({'success': True, 'data': employer_data_list})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})


class GetSpecificEmployerDataView(View):
    def get(self, request, employer_id, *args, **kwargs):
        try:
            # Fetch data for a specific employer based on the provided ID
            employer_data = Details.objects.filter(id=employer_id).values()

            # Check if the employer exists
            if not employer_data:
                return JsonResponse({'success': False, 'message': 'Employer not found'})

            # Convert the QuerySet to a list for serialization
            employer_data_list = list(employer_data)

            # Return the data as JSON
            return JsonResponse({'success': True, 'data': employer_data_list})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})


@csrf_exempt  # Use csrf_exempt for simplicity in this example; consider using csrf protection in production
def update_employer_account(request, employer_id):
    if request.method == 'POST':
        try:
            # Fetch the Details instance based on the provided employer_id
            employer = Details.objects.get(pk=employer_id)

            # Update the fields based on the received data
            employer.first_name = request.POST.get('first_name')
            employer.last_name = request.POST.get('last_name')
            employer.address = request.POST.get('address')
            employer.email = request.POST.get('email')
            employer.password = request.POST.get('pass')

            # Save the updated instance
            employer.save()

            # Return a success response
            return JsonResponse({'success': True, 'message': 'Employer details updated successfully'})

        except Details.DoesNotExist:
            # Return an error response if the employer_id doesn't exist
            return JsonResponse({'success': False, 'message': 'Employer not found'}, status=404)

    # Return an error response if the request method is not POST
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)


@csrf_exempt  # Use csrf_exempt for simplicity in this example; consider using csrf protection in production
def delete_employer_account(request, employer_id):
    if request.method == 'POST':
        try:
            # Fetch the Details instance based on the provided employer_id
            employer = Details.objects.get(pk=employer_id)

            # Delete the employer account
            employer.delete()

            # Return a success response
            return JsonResponse({'success': True, 'message': 'Employer account deleted successfully'})

        except Details.DoesNotExist:
            # Return an error response if the employer_id doesn't exist
            return JsonResponse({'success': False, 'message': 'Employer not found'}, status=404)

    # Return an error response if the request method is not POST
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)
