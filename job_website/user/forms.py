from django import forms
from .models import GraduateTracer

class GraduateTracerForm(forms.ModelForm):
    class Meta:
        model = GraduateTracer
        fields = '__all__'
        