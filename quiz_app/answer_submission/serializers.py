from rest_framework import serializers
from .models import AnswerSubmission
from quiz_management.models import Quiz
from user_management.models import Student
from question_management.models import Option

class AnswerSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerSubmission
        fields = ['quiz', 'student', 'option', 'is_correct', 'status']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"