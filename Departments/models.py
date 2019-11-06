from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class departments(models.Model):
    name = models.CharField(max_length=60)
    
