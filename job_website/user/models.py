from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True, default='email@email.com')
    password = models.CharField(max_length=255, default='password')
    
    def __str__(self):
        return self.username
    
# class Employee(models.Model):
#     email = models.EmailField(max_length=255, unique=True, default="email@email.com")
#     password = models.CharField(max_length=255, default='password')
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name

class Employee(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=255, default='user')
    last_name = models.CharField(max_length=255, default='')
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    civil_status = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, default="email@email.com")
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    region_of_origin = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    location_of_residence = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, default='password')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
