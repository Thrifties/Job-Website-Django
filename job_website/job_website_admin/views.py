from django.shortcuts import render

# Create your views here.

def dashboard_admin(request):
    template = 'dashboard_admin.html'
    return render(request, template)

def admin_list_of_jobs(request):
    template = 'admin_list_of_jobs.html'
    return render(request, template)