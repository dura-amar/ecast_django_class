from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name}'

class Destination(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    category=models.ManyToManyField(Category)
    def __str__(self):
        return f'{self.name}'
