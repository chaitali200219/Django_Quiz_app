from rest_framework import serializers
from .models import Quiz, Questions

class QuizSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(
        queryset=Questions.objects.all(),
        many=True,
        required=False
    )
    
    class Meta:
        model = Quiz
        fields = ['title', 'duration', 'status', 'questions']
