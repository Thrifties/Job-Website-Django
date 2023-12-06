from django import forms

from .models import Details
from .models import Job
from .models import Applicant
from .models import Company


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'