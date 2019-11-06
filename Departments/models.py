from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Departments(models.Model):
    name = models.CharField(max_length=60 blank=False)
    line_manager = models.CharField(max_length=60, blank=False)
    
    
    def __str__(self):
        return self.name

    def save_departments(self):
        self.save()

    def delete_departments(self):
        self.delete()  
        
    def update_departments(self):
        self.update()  
    
