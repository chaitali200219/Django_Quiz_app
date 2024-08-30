# results_management/serializers.py

from rest_framework import serializers
from .models import QuizResult, QuestionResult, LeaderboardEntry
from user_management.models import Student
from quiz_management.models import Quiz
from question_management.models import Questions, Option

class QuizResultSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.username', read_only=True)
    quiz = serializers.CharField(source='quiz.title', read_only=True)

    class Meta:
        model = QuizResult
        fields = ['id', 'student', 'quiz', 'score', 'date_taken']


class QuestionResultSerializer(serializers.ModelSerializer):
    quiz_result = serializers.CharField(source='quiz_result.id', read_only=True)
    question = serializers.CharField(source='question.content', read_only=True)
    selected_option = serializers.CharField(source='selected_option.content', read_only=True)

    class Meta:
        model = QuestionResult
        fields = ['id', 'quiz_result', 'question', 'selected_option', 'is_correct', 'marks_obtained']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.username', read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'student', 'total_score', 'last_updated']
