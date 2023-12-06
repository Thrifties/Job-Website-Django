from django.urls import path
from . import views
from .views import view_resume, applicant_list, approve_applicant, reject_applicant

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('post_job', views.post_job, name="post_job"),
    path('add_job', views.add_job, name="add_job"),
    path('applicants/', applicant_list, name="applicant_list"),
    path('applicants/resume/<str:resume_filename>/', view_resume, name='view_resume'),
    path('approve_applicant/<int:applicant_id>/', approve_applicant, name='approve_applicant'),
    path('reject_applicant/<int:applicant_id>/', reject_applicant, name='reject_applicant'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)