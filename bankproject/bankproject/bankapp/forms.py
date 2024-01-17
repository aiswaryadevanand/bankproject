from django import forms
from .models import District,Branch
class DistrictForm(forms.Form):
    district_data = forms.ModelChoiceField(queryset=District.objects.all(), empty_label=None)

class BranchForm(forms.Form):
    branch_data=forms.ModelChoiceField(queryset=Branch.objects.all(),empty_label=None)