from django.shortcuts import render

# Create your views here.


def dashboard(request):

    template = 'dashboard.html'
    context = {
        'title': 'Dashboard Page'
    }
    return render(request, template, context)
