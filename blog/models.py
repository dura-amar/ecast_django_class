from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=40)
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} - {self.author}'
    
    