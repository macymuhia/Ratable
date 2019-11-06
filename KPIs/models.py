from django.db import models

# Create your models here.

class Area(model.Model):
    name = models.CharField(max_length=50)

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