from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=60, blank=False)
   
    
    def __str__(self):
        return self.name

    def save_departments(self):
        self.save()
        
    def delete_departments(self):
        self.delete()  
        
    def edit_departments(self):
        self.edit()
        
class Staff(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
    

