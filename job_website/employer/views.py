from django.shortcuts import render, redirect
from .models import Job
from .models import Applicant
from django.http import FileResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def dashboard(request):

    template = 'dashboard.html'
    context = {
        'title': 'Dashboard Page'
    }
    return render(request, template, context)


def post_job(request):

    template = 'post_job.html'
    context = {
        'title': 'Post Job Page'
    }
    return render(request, template, context)


def add_job(request):
    if request.method == 'POST':
        # Access form data directly from request.POST
        title = request.POST.get('title')
        number_of_people = request.POST.get('number_of_people')
        salary = request.POST.get('salary')
        category = request.POST.get('category')
        location = request.POST.get('location')
        description = request.POST.get('description')
        date = request.POST.get('date')
        requirement1 = 'requirement1' in request.POST
        requirement2 = 'requirement2' in request.POST
        requirement3 = 'requirement3' in request.POST

        # Create a new Job instance and save to the database
        Job.objects.create(
            title=title,
            number_of_people=number_of_people,
            salary=salary,
            category=category,
            location=location,
            description=description,
            date=date,
            requirement1=requirement1,
            requirement2=requirement2,
            requirement3=requirement3
        )

        # Redirect to a success page or do something else
        # Adjust 'success_page' to your actual success page URL
        return redirect('post_job')

    context = {
        'title': 'Post Job Page',
    }

    return render(request, 'post_job.html', context)


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