# results_management/serializers.py

from rest_framework import serializers
from .models import QuizResult, QuestionResult, LeaderboardEntry
from user_management.models import Student
from quiz_management.models import Quiz
from question_management.models import Questions, Option
from answer_submission.models import AnswerSubmission  # Import AnswerSubmission model
from django.db.models import Sum

class QuizResultSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.username', read_only=True)
    quiz = serializers.CharField(source='quiz.title', read_only=True)
    questions = serializers.SerializerMethodField()

    class Meta:
        model = QuizResult
        fields = ['id', 'student', 'quiz', 'score', 'date_taken', 'questions']

    def get_questions(self, obj):
        """
        Retrieve all the answer submissions related to the quiz result.
        """
        submissions = AnswerSubmission.objects.filter(student=obj.student, quiz=obj.quiz)
        return AnswerSubmissionSerializer(submissions, many=True).data


class AnswerSubmissionSerializer(serializers.ModelSerializer):
    """
    Serializer for the AnswerSubmission model to be included in the QuizResultSerializer.
    """
    question = serializers.CharField(source='option.question.content', read_only=True)
    option = serializers.CharField(source='option.content', read_only=True)

    class Meta:
        model = AnswerSubmission
        fields = ['id', 'quiz', 'student', 'question', 'option', 'is_correct', 'status']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.username', read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'student', 'total_score', 'last_updated']
