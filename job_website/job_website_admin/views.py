from django.shortcuts import render, redirect
from employer.models import Job

# Create your views here.


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
