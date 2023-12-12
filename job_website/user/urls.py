from django.urls import path
from . import views
from .views import company
from .views import user_company_profile

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('company/', company, name='company'),
    path('user_company_profile/<int:id>/', user_company_profile, name='user_company_profile'),
    path('user_register', views.user_register, name='user_register'),
    path('add_user', views.add_user, name='add_user'),
    path('user_login', views.user_login, name='user_login'),
    path('user_toLogin', views.user_toLogin, name='user_toLogin'),
    path('user_toLogout', views.user_toLogout, name='user_toLogout'),
    path('user_application_process/<int:id>/', views.user_application_process,name='user_application_process'),
    path('user_apply_job', views.user_apply_job, name='user_apply_job'),
    path('user_my_jobs', views.user_my_jobs, name='user_my_jobs'),
]