from rest_framework import serializers
from .models import AnswerSubmission
from user_management.models import Student
from question_management.models import Questions,Option
from quiz_management.models import Quiz

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"

class AnswerSubmissionSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Questions.objects.all())
    option = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all())

    class Meta:
        model = AnswerSubmission
        fields = ['quiz', 'student', 'option', 'question', 'is_correct', 'status']
