from django.urls import path
from . import views


urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
]
