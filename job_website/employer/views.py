from django.shortcuts import render, redirect
from .models import Job
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
