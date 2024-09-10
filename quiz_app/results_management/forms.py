from django import forms
from .models import QuizResult

class QuizResultForm(forms.ModelForm):
    class Meta:
        model = QuizResult
        fields = ['student', 'quiz', 'score']
