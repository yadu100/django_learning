from django.forms import ModelForm
from .models import EmployeeDatabase
from django import forms

class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeDatabase
        fields = '__all__'

        widgets = {
            'user' : forms.Select(attrs={'class': 'form-control border-primary w-50 m-auto text-center'}),
            'name': forms.TextInput(attrs={'class':'form-control border-primary w-50 m-auto'}),
            'employee_id' : forms.TextInput(attrs={'class': 'form-control border-primary w-50 m-auto'}),
            'designation' : forms.TextInput(attrs={'class': 'form-control border-primary w-50 m-auto'}),
            'department' : forms.TextInput(attrs={'class' : 'form-control border-primary w-50 m-auto'}),
            'salaryLPA' : forms.TextInput(attrs={'class' : 'form-control border-primary w-50 m-auto'}),
            'profile_img' : forms.ClearableFileInput(attrs={'class' : 'form-control-file border-primary w-50 m-auto', 'type':'file'}),
            'total_experience' : forms.Select(attrs={'class': 'form-control border-primary w-50 m-auto'}),
            'skillset' : forms.SelectMultiple(attrs={'class':'form-control border-primary w-50 m-auto'}),                                         
                                                     
        }