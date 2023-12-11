from django.urls import path
from . import views


urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('user_register', views.user_register, name='user_register'),
    path('add_user', views.add_user, name='add_user'),
    path('user_login', views.user_login, name='user_login'),
    path('user_toLogin', views.user_toLogin, name='user_toLogin'),
    path('user_toLogout', views.user_toLogout, name='user_toLogout'),
    path('user_application_process', views.user_application_process,
         name='user_application_process'),
]
