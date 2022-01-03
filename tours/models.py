from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name}'

class District(models.Model):
    dname=models.CharField(max_length=30)
    area=models.FloatField()
    def __str__(self):
        return self.dname

class Destination(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    category=models.ManyToManyField(Category)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'


    
