from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('post_job', views.post_job, name="post_job"),
    path('add_job', views.add_job, name="add_job"),
    path('company_profile', views.company_profile, name="company_profile"),
    path('register', views.register, name="register"),
    path('add_employer', views.add_employer, name="add_employer"),
    path('profile_settings', views.profile_settings, name="profile_settings")
]

