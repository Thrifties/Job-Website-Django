from django.shortcuts import render

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
