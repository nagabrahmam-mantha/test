from django.forms import ModelForm, TextInput, NumberInput, DateInput, Textarea, Select
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["first_name", "last_name", "birthdate"]