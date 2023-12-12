from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('user_register', views.user_register, name='user_register'),
    path('add_user', views.add_user, name='add_user'),
    path('user_login', views.user_login, name='user_login'),
    path('user_toLogin', views.user_toLogin, name='user_toLogin'),
    path('graduate_tracer', views.graduate_tracer, name='graduate_tracer'),
    path('add_tracer', views.add_tracer, name='add_tracer'),
    
]