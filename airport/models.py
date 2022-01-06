from django.db import models

# Create your models here.
class Airport(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    image=models.ImageField()
    
    def __str__(self):
        return self.name