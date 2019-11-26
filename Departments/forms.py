from django import forms
from Departments.models import *


class DepartmentCreationForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name', 'description']


class EditDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']
