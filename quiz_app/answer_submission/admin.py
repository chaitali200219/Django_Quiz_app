from django.contrib import admin
from .models import AnswerSubmission

# Register your models here.

@admin.register(AnswerSubmission)
class AnswerAubmissionAdmin(admin.ModelAdmin):
    list_display = ('id','student', 'option', 'status','is_correct')