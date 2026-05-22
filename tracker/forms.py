from django import forms
from .models import Med

class MedForm(forms.ModelForm):
    class Meta:
        model = Med
        fields = ["name","dosage","unit","daily_amount","total_amount","start_date","expiration_date","notes"]

        widgets = {"start_date": forms.DateInput(attrs={"type":"date"}),"expiration_date": forms.DateInput(attrs={"type":"date"})}
