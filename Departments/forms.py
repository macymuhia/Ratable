from django import forms
from Departments.models import Department


class DepartmentCreationForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name']
