from django.shortcuts import render, redirect

# Create your views here.

def homepage(request):
    template = 'user_homepage.html'
    context = {
        'title' : 'Homepage',
    }
    return render(request, template, context)