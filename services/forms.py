from django import forms
from .models import Client, Service, TechnicalReport

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'service_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TechnicalReportForm(forms.ModelForm):
    class Meta:
        model = TechnicalReport
        fields = '__all__'
        widgets = {
            'diagnosis': forms.Textarea(attrs={'rows': 4}),
            'interventions': forms.Textarea(attrs={'rows': 4}),
            'parts_used': forms.Textarea(attrs={'rows': 3}),
            'recommendations': forms.Textarea(attrs={'rows': 3}),
        }