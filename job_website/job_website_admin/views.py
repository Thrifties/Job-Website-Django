from django.shortcuts import render
from employer.models import Job, Applicant, Details

# Create your views here.

def dashboard_admin(request):
    first_name = Details.objects.get().first_name
    template = 'dashboard_admin.html'
    context = {
        'first_name': first_name,
    }
    return render(request, template, context)

def admin_list_of_jobs(request):
    template = 'admin_list_of_jobs.html'
    return render(request, template)