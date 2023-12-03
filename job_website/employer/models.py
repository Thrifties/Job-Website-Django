from django.db import models

# Create your models here.

class Details(models.Model):
    
    name = models.CharField(max_length=50, default="")
    company = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=10, default="")
    password = models.CharField(max_length=50, default="")
    
    def __str__(self):
        return self.name
    
class Job(models.Model):
    title = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=50, default="")
    salary = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=1000, default="")
    requirements = models.CharField(max_length=1000, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=10, default="")
    date = models.DateField()
    
    def __str__(self):
        return self.title
    
class Applicant(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=100, default="")
    resume = models.FileField(upload_to='employer/applicants/resume/')
    company = models.CharField(max_length=50, default="")
    job = models.CharField(max_length=50, default="")
    application_status = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=application_status, default='Pending')
    
    def __str__(self):
        return self.name