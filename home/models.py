from django.db import models

# Create your models here.

class Introduction(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    college=models.CharField(max_length=100)
    
class Subject(models.Model):
    title=models.CharField(max_length=100)
    subject_code=models.IntegerField()
    
    