from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('company', views.company, name='company'),
    path('user_register', views.user_register, name='user_register'),
    path('add_user', views.add_user, name='add_user'),
    path('user_login', views.user_login, name='user_login'),
    path('user_toLogin', views.user_toLogin, name='user_toLogin'),
]