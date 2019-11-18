from django import forms
from Departments.models import Department


class DepartmentCreationForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name']
        
class EditDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
        
# class NameForm(forms.ModelForm):
#     class Meta:
#         model =Department
#         fields = ['name','line_manager']

