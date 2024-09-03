# results_management/admin.py

from django.contrib import admin
from .models import QuizResult, LeaderboardEntry

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'date_taken')
    readonly_fields = ('score',)

    def save_model(self, request, obj, form, change):
        if not change:  # If creating a new object
            obj.calculate_score()
        super().save_model(request, obj, form, change)

@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_score', 'last_updated')
    readonly_fields = ('total_score',)

    def save_model(self, request, obj, form, change):
        obj.update_total_score()  # Automatically update total score
        super().save_model(request, obj, form, change)
