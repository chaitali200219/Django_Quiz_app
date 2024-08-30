from rest_framework import serializers
from .models import Questions

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'content', 'question_type', 'marks', 'created_at', 'created_by']
