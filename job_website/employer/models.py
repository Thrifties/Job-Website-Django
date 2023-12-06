from django.db import models

# Create your models here.


class Details(models.Model):

    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    company = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=10, default="")
    password = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class JobStatus(models.TextChoices):
    OPEN = 'Open', 'Open'
    CLOSED = 'Closed', 'Closed'


class Job(models.Model):
    title = models.CharField(max_length=255, default="")
    # Set a valid default numerical value
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
        default=JobStatus.OPEN)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=10, default="")
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

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField()
    location = models.CharField(max_length=255)
    website = models.URLField()
    scope = models.CharField(max_length=255)
    overview = models.TextField()
    join_us = models.TextField()

    def __str__(self):
        return self.company_name
