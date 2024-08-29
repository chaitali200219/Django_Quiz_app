from django.contrib import admin
from .models import Questions, Option

@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'question_type', 'marks', 'created_at','created_by')

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'content', 'is_correct', 'status')

