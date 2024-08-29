from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from user_management.models import Teacher


# Create your models here.



class Questions(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('MCQ', _('Multiple Choice')),
        ('True', _('True')),
        ('False', _('False')),
    ]
    # question_id=models.AutoField(primary_key=True)
    # text of the question is content
    content=models.CharField(max_length=255)
    # type of the question rather mcq or t/f
    question_type=models.CharField(max_length=50,choices=QUESTION_TYPE_CHOICES)
    # marks allocated to each questions
    marks = models.PositiveIntegerField()
    # timestamp when the question was created
    created_at=models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='questions',null=True)
    
    
    def __str__(self):
        return self.content
    
    
class Option(models.Model):
    STATUS_CHOICES=[
        ('active',_('Active')),
        ('inactive',_('Inactive')),
    ]    
    # Option_id=models.AutoField(primary_key=True)
    # key field linking with questions
    question=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name="options")
    # text field
    content = models.CharField(max_length=255)
    # check whether the option is correct or not
    is_correct = models.BooleanField(default=False)
    # active or inactive
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.content
    


# class Tag(models.Model):
#     tag_id=models.AutoField(primary_key=True)
#     # each tag realted to one question
#     question=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='tags')
#     tag_name=models.CharField(max_length=100)
#     # type of question which is assocaited with teh tag
#     question_type=models.CharField(max_length=50)
    
    
#     def __str__(self):
#         return self.tag_name