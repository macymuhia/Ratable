from django.db import models
from django.contrib.auth.models import User
from Departments.models import Department


# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name

    def save_area(self):
        '''
        method used the save the areas added.
        '''
        self.save()
        

    def delete_area(self):
        '''
        method used the delete the areas added.
        '''
        self.delete()


    def update_area(self):
        '''
        method used the update the areas added.
        '''
        self.update()

    @classmethod
    def get_areas(cls):
        areas = cls.objects.all()
        return areas



class Indicators(models.Model):
    name = models.CharField(max_length=30)
    area = models.ForeignKey(Area,on_delete=models.CASCADE,null=True)
    line_manager_score = models.FloatField(default=0)
    staff_score =  models.FloatField(default=0)

    class Meta:
        ordering=['area']
        
    def __str__(self):
        return self.name

    def save_indica(self):
        self.save()
    
    def update_indica(self):
        self.update()
    
    def delete_indica(self):
        self.delete()

    @classmethod
    def get_indicators(cls):
        indicators = cls.objects.all()
        return indicators


class Score(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    indicators = models.ForeignKey(Indicators, on_delete=models.CASCADE, null=True)

    def save_score(self):
        self.save()

# This will hold the processed logic for our reports. 
class Reports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    area_average = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    overall_score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)

    def __str__(self):
        return self.overall_score

    def save_report(self):
        self.save()