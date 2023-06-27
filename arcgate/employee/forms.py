
from django.forms import ModelForm

from employee.models import Employee, Profile

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
        