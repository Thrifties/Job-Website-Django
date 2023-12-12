from django.urls import path
from . import views
from .views import company
from .views import profile
from .views import user_company_profile
from .views import get_employee_data
from .views import UpdateEmployeeProfile
from .views import add_educational_background
from .views import fetch_educational_background
from .views import add_career_history
from .views import fetch_career_history
from .views import add_advance_studies
from .views import fetch_advance_studies
from .views import add_advance_reason
from .views import fetch_advance_reasons
from .views import add_skill
from .views import fetch_skills
from .views import add_professional_examination, fetch_professional_examinations
from .views import delete_educational_background
from .views import delete_career_history
from .views import delete_advance_studies
from .views import delete_advance_reason
from .views import delete_skill
from .views import delete_professional_examination
from .views import update_profile_picture

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('company/', company, name='company'),
    path('profile/', profile, name='profile'),
    path('get_employee_data/<int:employee_id>/', get_employee_data, name='get_employee_data'),
    path('update_employee_profile/<int:employee_id>/', UpdateEmployeeProfile.as_view(), name='update_employee_profile'),
    path('add_educational_background/', add_educational_background, name='add_educational_background'),
    path('fetch_educational_background/', fetch_educational_background, name='fetch_educational_background'),
    path('add_career_history/', add_career_history, name='add_career_history'),
    path('fetch_career_history/', fetch_career_history, name='fetch_career_history'),
    path('add_advance_studies/', add_advance_studies, name='add_advance_studies'),
    path('fetch_advance_studies/', fetch_advance_studies, name='fetch_advance_studies'),
    path('add_advance_reason/', add_advance_reason, name='add_advance_reason'),
    path('fetch_advance_reasons/', fetch_advance_reasons, name='fetch_advance_reasons'),
    path('add_skill/', add_skill, name='add_skill'),
    path('fetch_skills/', fetch_skills, name='fetch_skills'),
    path('add_professional_examination/', add_professional_examination, name='add_professional_examination'),
    path('fetch_professional_examinations/', fetch_professional_examinations, name='fetch_professional_examinations'),
    path('delete_educational_background/', delete_educational_background, name='delete_educational_background'),
    path('delete_career_history/', delete_career_history, name='delete_career_history'),
    path('delete_advance_studies/', delete_advance_studies, name='delete_advance_studies'),
    path('delete_advance_reason/', delete_advance_reason, name='delete_advance_reason'),
    path('delete_skill/', delete_skill, name='delete_skill'),
    path('delete_professional_examination/', delete_professional_examination, name='delete_professional_examination'),
    path('user_company_profile/<int:id>/', user_company_profile, name='user_company_profile'),
    path('user_register', views.user_register, name='user_register'),
    path('add_user', views.add_user, name='add_user'),
    path('user_login', views.user_login, name='user_login'),
    path('user_toLogin', views.user_toLogin, name='user_toLogin'),
    path('user_toLogout', views.user_toLogout, name='user_toLogout'),
    path('user_application_process/<int:id>/', views.user_application_process,name='user_application_process'),
    path('user_apply_job', views.user_apply_job, name='user_apply_job'),
    path('update_profile_picture/', update_profile_picture, name='update_profile_picture'),
    path('graduate_tracer', views.graduate_tracer, name='graduate_tracer'),
    path('add_tracer', views.add_tracer, name='add_tracer'),
    
]


