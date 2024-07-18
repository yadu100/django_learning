from django.forms import ModelForm
from .models import EmployeeDatabase

class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeDatabase
        fields = '__all__'