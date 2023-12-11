from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Details(models.Model):

    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    company = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=11, default="")
    password = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.first_name


class JobStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    REJECTED = 'Reject', 'Reject'
    OPEN = 'Open', 'Open'
    CLOSED = 'Closed', 'Closed'


class Job(models.Model):
    company = models.CharField(max_length=255, default="")
    title = models.CharField(max_length=255, default="")
    number_of_people = models.IntegerField(default=0)
    salary = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=255, default="")
    location = models.CharField(max_length=255, default="")
    description = models.TextField(max_length=255, default="")
    date = models.DateField(default=None)  # Or set a default date if needed
    requirements = models.CharField(max_length=255, default="")
    status = models.CharField(
        max_length=10,
        choices=JobStatus.choices,
        default=JobStatus.PENDING)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=11, default="")
    address = models.CharField(max_length=100, default="")
    resume = models.FileField(upload_to='employer/applicants/resume/')
    company = models.CharField(max_length=50, default="")
    job = models.CharField(max_length=50, default=" ")
    application_status = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=10, choices=application_status, default='Pending')
    rejection_reason = models.TextField(blank=True, null=True)
    approval_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=255, default='-', blank=False)
    company_email = models.EmailField(default='-', blank=False)
    location = models.CharField(max_length=255, default='-', blank=False)
    website = models.URLField(default='-', blank=False)
    scope = models.CharField(max_length=255, default='-', blank=False)
    overview = models.TextField(default='-', blank=False)
    join_us = models.TextField(default='-', blank=False)
    profile_picture_path = models.CharField(
        max_length=255, default='', blank=True)
    cover_photo_path = models.CharField(max_length=255, default='', blank=True)
    employerID = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.company_name
