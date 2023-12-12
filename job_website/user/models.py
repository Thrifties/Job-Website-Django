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
    profile_picture_path = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.email

class EducationalBackground(models.Model):
    degree = models.CharField(max_length=100)  # Allow users to type their own degree
    college_or_university = models.CharField(max_length=255)
    year_graduated = models.PositiveIntegerField()
    honors_or_awards = models.TextField(blank=True, null=True)
    employee_id = models.CharField(max_length=20)  # Assuming employeeId is a string, adjust if it's a different type

    def __str__(self):
        return f"{self.degree} from {self.college_or_university} ({self.year_graduated})"

from django.db import models

class CareerHistory(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    started = models.DateField()
    ended = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    employee_id = models.CharField(max_length=20)  # Assuming employeeId is a string, adjust if it's a different type

    def __str__(self):
        return f"{self.job_title} at {self.company_name} ({self.started} to {self.ended})"

from django.db import models

class AdvanceStudies(models.Model):
    training_title = models.CharField(max_length=100)
    training_institution = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    credits_earned = models.PositiveIntegerField()
    employee_id = models.CharField(max_length=20)  # Assuming employeeId is a string, adjust if it's a different type

    def __str__(self):
        return f"{self.training_title} at {self.training_institution} ({self.duration})"


class AdvanceReason(models.Model):
    training_reason = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=20)  # Assuming employeeId is a string, adjust if it's a different type

    def __str__(self):
        return self.training_reason
    
class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20)  # Assuming employee_id is a string, adjust if it's a different type

    def __str__(self):
        return self.skill_name

class ProfessionalExamination(models.Model):
    exam_title = models.CharField(max_length=255)
    exam_date = models.DateField()
    exam_rating = models.FloatField()
    employee_id = models.CharField(max_length=20)  # Assuming employeeId is a string, adjust if it's a different type

    def __str__(self):
        return f"{self.exam_title} taken on {self.exam_date} by Employee ID: {self.employee_id}"


class MyJobs(models.Model):
    name = models.CharField(max_length=255, default='name')
    job = models.CharField(max_length=255, default='job')
    company = models.CharField(max_length=255, default='company')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name