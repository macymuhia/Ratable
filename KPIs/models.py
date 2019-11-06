from django.db import models

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

class Indicators(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_indica(self):
        self.save()
    
    def update_indica(self):
        self.update()
    
    def delete_indica(self):
        self.delete()



