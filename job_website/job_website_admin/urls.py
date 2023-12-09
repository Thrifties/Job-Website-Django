from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard_admin', views.dashboard_admin, name='dashboard_admin'),
    path('admin_list_of_jobs', views.admin_list_of_jobs, name='admin_list_of_jobs'),
    path('approve_job/<int:job_id>/', views.approve_job, name='approve_job'),
    path('reject_job/<int:job_id>/', views.reject_job, name='reject_job'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('index', views.index, name='index'),
]
