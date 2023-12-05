from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('post_job', views.post_job, name="post_job"),
    path('add_job', views.add_job, name="add_job"),
    path('get_job_details', views.get_job_details, name='get_job_details'),
    path('save_job_changes', views.save_job_changes, name='save_job_changes'),
]
