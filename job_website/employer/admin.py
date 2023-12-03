from django.contrib import admin
from .models import Details
from .models import Job
from .models import Applicant
# Register your models here.

admin.site.register(Details)
admin.site.register(Job)
admin.site.register(Applicant)