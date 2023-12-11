
from django.shortcuts import render, redirect
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Employee
from django.shortcuts import render, get_object_or_404
from employer.models import Job
from django.views import View
from django.db.models import Q
# Create your views here.


def homepage(request):
    # Fetch all jobs from the Job model
    jobs = Job.objects.all()

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        jobs = jobs.filter(Q(title__icontains=search_query))

    # Pass the jobs to the template context
    context = {
        'title': 'Homepage',
        'jobs': jobs,
    }

    # Render the template with the provided context
    return render(request, 'user_homepage.html', context)


def job_detail(request, job_id):
    # Retrieve the job details using the job_id
    job = get_object_or_404(Job, id=job_id)

    # Pass the job details to the template context
    context = {
        'title': f'{job.title} - Job Detail',
        'job': job,
    }

    # Render the template with the provided context
    return render(request, 'job_detail.html', context)
