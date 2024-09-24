from django.contrib import admin
from .models import Quiz

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'duration', 'status', 'created_at','created_by')
    list_filter = ('status', 'created_at')
    search_fields = ('title',)
    ordering = ('created_at',)

# Register your models here.
