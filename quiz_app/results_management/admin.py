from django.contrib import admin
from .models import QuizResult

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'date_taken')
