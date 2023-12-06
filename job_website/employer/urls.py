from django.urls import path
from . import views
from .views import view_resume, applicant_list, approve_applicant, reject_applicant

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('post_job', views.post_job, name="post_job"),
    path('add_job', views.add_job, name="add_job"),
    path('get_job_details', views.get_job_details, name='get_job_details'),
    path('save_job_changes', views.save_job_changes, name='save_job_changes'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('company_profile', views.company_profile, name="company_profile"),
    path('add_company_profile', views.add_company_profile,name="add_company_profile"),
    path('register', views.register, name="register"),
    path('add_employer', views.add_employer, name="add_employer"),
    path('profile_settings', views.profile_settings, name="profile_settings"),
    path('login', views.login, name='login'),
    path('add_job', views.add_job, name="add_job"),
    path('applicants/', applicant_list, name="applicant_list"),
    path('applicants/resume/<str:resume_filename>/', view_resume, name='view_resume'),
    path('approve_applicant/<int:applicant_id>/', approve_applicant, name='approve_applicant'),
    path('reject_applicant/<int:applicant_id>/', reject_applicant, name='reject_applicant'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)