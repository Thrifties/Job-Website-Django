from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('post_job', views.post_job, name="post_job"),
    path('add_job', views.add_job, name="add_job"),
    path('register', views.register, name="register"),
    path('add_employer', views.add_employer, name="add_employer")
]
