from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard_admin', views.dashboard_admin, name='dashboard_admin'),
    path('admin_list_of_jobs', views.admin_list_of_jobs, name='admin_list_of_jobs'),
]