from django import forms

from .models import Details
from .models import Job
from .models import Applicant


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'number_of_people', 'salary', 'category', 'location',
                  'description', 'date', 'requirement1', 'requirement2', 'requirement3']