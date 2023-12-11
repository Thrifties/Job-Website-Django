from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True, default='email@email.com')
    password = models.CharField(max_length=255, default='password')
    
    def __str__(self):
        return self.username
    
class Employee(models.Model):
    email = models.EmailField(max_length=255, unique=True, default="email@email.com")
    password = models.CharField(max_length=255, default='password')
    first_name = models.CharField(max_length=255, default='first_name')
    last_name = models.CharField(max_length=255, default='last_name')
    phone_number = models.CharField(max_length=255, default='phone_number')
    address = models.CharField(max_length=255, default='address')
    def __str__(self):
        return self.email
    
class MyJobs(models.Model):
    name = models.CharField(max_length=255, default='name')
    job = models.CharField(max_length=255, default='job')
    company = models.CharField(max_length=255, default='company')
    
    def __str__(self):
        return self.job