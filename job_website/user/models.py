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
        return self.email
    
class MyJobs(models.Model):
    name = models.CharField(max_length=255, default='name')
    job = models.CharField(max_length=255, default='job')
    company = models.CharField(max_length=255, default='company')
    status = models.CharField(max_length=255, default='status')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class GraduateTracer(models.Model):
    # Personal Information
    college = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    year_graduated = models.IntegerField(choices=[(year, str(year)) for year in range(1950, 2031)])
    address = models.CharField(max_length=255)
    civil_status = models.CharField(max_length=20, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')])
    age = models.CharField(max_length=3)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=11)
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    # Education Attained
    education_attained = models.CharField(max_length=50, choices=[
        ('Certificate in Two Year Course', 'Certificate in Two Year Course'),
        ('College graduate', 'College graduate'),
        ('With Units in Masters Degree', 'With Units in Masters Degree'),
        ('Masters Degree Holder', 'Masters Degree Holder'),
        ('With Units in Doctoral Degree', 'With Units in Doctoral Degree'),
        ('Doctoral Degree Holder', 'Doctoral Degree Holder'),
    ])
    # Scholarship Information
    scholarship_recipient = models.CharField(max_length=100, choices=[
        ('Yes, I am recipient of Government scholarship program', 'Yes, I am recipient of Government scholarship program'),
        ('Yes, I am recipient of private scholarship program', 'Yes, I am recipient of private scholarship program'),
        ('No, I am not recipient of any scholarship program', 'No, I am not recipient of any scholarship program'),
    ])
    # Employment Information
    presently_employed = models.CharField(max_length=20, choices=[('Yes with employer', 'Yes with employer'), ('Yes self-employed', 'Yes self-employed'), ('No', 'No')])
    organization_or_employer = models.CharField(max_length=255)
    organization_type = models.CharField(max_length=20, choices=[
        ('Public/Government', 'Public/Government'),
        ('NGO', 'NGO'),
        ('Non-profit', 'Non-profit'),
        ('Private Owned', 'Private Owned'),
    ])
    employment_status = models.CharField(max_length=20, choices=[
        ('Regular/Permanent', 'Regular/Permanent'),
        ('Temporary', 'Temporary'),
        ('Casual', 'Casual'),
        ('Contractual', 'Contractual'),
        ('Self-employed', 'Self-employed'),
    ])
    work_location = models.CharField(max_length=10, choices=[('Local', 'Local'), ('Abroad', 'Abroad')])
    current_occupation = models.CharField(max_length=255)
    years_in_company = models.CharField(max_length=3)
    major_line_of_business = models.CharField(max_length=50, choices=[
        ('BPO', 'BPO'),
        ('Trade/Industry', 'Trade/Industry'),
        ('Legal', 'Legal'),
        ('Telecom/Communications', 'Telecom/Communications'),
        ('IT/Computer/Software', 'IT/Computer/Software'),
        ('Banking and Finance', 'Banking and Finance'),
        ('Insurance', 'Insurance'),
        ('Services', 'Services'),
        ('Government', 'Government'),
        ('Academic', 'Academic'),
        ('Manufacturing', 'Manufacturing'),
        ('Other', 'Other'),
    ])
    # Reasons to Stay in the Job
    reason_to_stay = models.CharField(max_length=255)
    # Salary Information
    gross_monthly_rate = models.CharField(max_length=20, choices=[
        ('Below P 10,000', 'Below P 10,000'),
        ('P 10,000 to P 20,000', 'P 10,000 to P 20,000'),
        ('P 21,000 to P 30,000', 'P 21,000 to P 30,000'),
        ('P 31,000 to P 40,000', 'P 31,000 to P 40,000'),
        ('P 41,000 to P 50,000', 'P 41,000 to P 50,000'),
        ('P 51,000 to P 60,000', 'P 51,000 to P 60,000'),
        ('P 61,000 to P 70,000', 'P 61,000 to P 70,000'),
        ('Above P 71,000', 'Above P 71,000'),
    ])
    # Additional Information
    award = models.CharField(max_length=255)
    key_position = models.CharField(max_length=255)
    course_related_to_job = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    first_job_found_duration = models.CharField(max_length=20, choices=[
        ('Less than a month', 'Less than a month'),
        ('1-3 months', '1-3 months'),
        ('3-6 months', '3-6 months'),
        ('6-12 months', '6-12 months'),
        ('Above 1 year', 'Above 1 year'),
        ('Above 3 years', 'Above 3 years'),
    ])
    first_job_present = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    first_job_stay_duration = models.CharField(max_length=50, choices=[
        ('Less than a month', 'Less than a month'),
        ('1-3 months', '1-3 months'),
        ('3-6 months', '3-6 months'),
        ('6-12 months', '6-12 months'),
        ('Above 1 year', 'Above 1 year'),
        ('Still working on the first job', 'Still working on the first job'),
    ])
    known_first_job_through = models.CharField(max_length=50, choices=[
        ('Response to advertisement', 'Response to advertisement'),
        ('Arranged by school\'s job placement offer', 'Arranged by school\'s job placement offer'),
        ('Walk-in applicant', 'Walk-in applicant'),
        ('Family business', 'Family business'),
        ('Recommended by someone', 'Recommended by someone'),
        ('Info from friends', 'Info from friends'),
        ('Other', 'Other'),
    ])
    first_job_level_position = models.CharField(max_length=50, choices=[
        ('Rank or clerical', 'Rank or clerical'),
        ('Professional, technical, or supervisory', 'Professional, technical, or supervisory'),
        ('Managerial or executive', 'Managerial or executive'),
        ('Self-employed', 'Self-employed'),
    ])
    gross_monthly_earning_first_job = models.CharField(max_length=20, choices=[
        ('Below P 10,000', 'Below P 10,000'),
        ('P 10,000 to P 20,000', 'P 10,000 to P 20,000'),
        ('P 21,000 to P 30,000', 'P 21,000 to P 30,000'),
        ('P 31,000 to P 40,000', 'P 31,000 to P 40,000'),
        ('P 41,000 to P 50,000', 'P 41,000 to P 50,000'),
        ('P 51,000 to P 60,000', 'P 51,000 to P 60,000'),
        ('P 61,000 to P 70,000', 'P 61,000 to P 70,000'),
        ('Above P 71,000', 'Above P 71,000'),
    ])
    curriculum_related_to_first_job = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    # Competency Ratings
    communication_skills = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    human_relations_skills = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    entrepreneurial_skills = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    information_technology_skills = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    problem_solving_skills = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    critical_thinking_skills = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    def __str__(self):
        return self.name