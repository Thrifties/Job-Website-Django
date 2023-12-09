from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import GetEmployerDataView
from .views import GetSpecificEmployerDataView
from .views import update_employer_account
from .views import delete_employer_account

urlpatterns = [
    path('admin_list_of_jobs', views.admin_list_of_jobs, name='admin_list_of_jobs'),
    path('approve_job/<int:job_id>/', views.approve_job, name='approve_job'),
    path('reject_job/<int:job_id>/', views.reject_job, name='reject_job'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('get_employer_data/', GetEmployerDataView.as_view(), name='get_employer_data'),
    path('update_employer_account/<int:employer_id>/', update_employer_account, name='update_employer_account'),
     path('delete_employer_account/<int:employer_id>/', delete_employer_account, name='delete_employer_account'),
    path('manage_account', views.manage_account, name='manage_account'),
    path('get_specific_employer_data/<int:employer_id>/', GetSpecificEmployerDataView.as_view(), name='get_specific_employer_data'),
    path('index', views.index, name='index'),
]
