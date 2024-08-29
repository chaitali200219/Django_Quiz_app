from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience_years = models.PositiveIntegerField()

            
            
    def __str__(self):
        return self.user.first_name
    


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=25)
    
    def __str__(self):
        return self.user.first_name
    
    def save(self, *args, **kwargs):
        if Student.objects.filter(user=self.user).exists():
            raise ValueError("Teacher cannot be a student")
        else : 
             super().save(*args, **kwargs)
    
    
    
