from django import forms
from .models import Driver, Company


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["name", "phone_number", "state", "rate", "age", "nationality", "experience"]



class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "phone_number", "location", "state", "rate_cpm", "rate_per", "age", "nationality", "experience"]
        