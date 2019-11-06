from django import forms
from .models import Departments

class DepartmentCreationForm(forms.Form):
    
    model = Department
    fields = ['name', 'line_manager']