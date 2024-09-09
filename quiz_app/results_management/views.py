from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from .models import QuizResult, LeaderboardEntry
from .serializers import QuizResultSerializer, LeaderboardEntrySerializer
from answer_submission.models import AnswerSubmission
from user_management.models import Student
from quiz_management.models import Quiz


class SubmitQuizView(APIView):
    """
    This view handles the submission of quiz answers, calculates the result, and updates the leaderboard.
    """
    permission_classes = [IsAuthenticated]  # Require authentication
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication

    def post(self, request, *args, **kwargs):
        student_id = request.data.get('student_id')
        quiz_id = request.data.get('quiz_id')

        # Retrieve the student and quiz objects
        student = get_object_or_404(Student, id=student_id)
        quiz = get_object_or_404(Quiz, id=quiz_id)

        # Create or update the QuizResult for this student and quiz
        quiz_result, created = QuizResult.objects.get_or_create(student=student, quiz=quiz)

        # Fetch all related submissions
        submissions = AnswerSubmission.objects.filter(student=student, quiz=quiz, status='submitted')
        correct_answers = submissions.filter(is_correct=True).count()

        # Update the score based on correct answers
        quiz_result.score = correct_answers
        quiz_result.save()

        # Update the leaderboard entry
        leaderboard_entry, created = LeaderboardEntry.objects.get_or_create(student=student)
        leaderboard_entry.update_total_score()

        # Serialize and return the quiz result
        serializer = QuizResultSerializer(quiz_result)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# View to list all quiz results or create a new quiz result
class QuizResultListView(generics.ListCreateAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer
    permission_classes = [IsAuthenticated]  # Require authentication
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication


# View to retrieve, update, or delete a specific quiz result
class QuizResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer
    permission_classes = [IsAuthenticated]  # Require authentication
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication


# View to list leaderboard entries
class LeaderboardEntryListView(generics.ListAPIView):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer
    permission_classes = [IsAuthenticated]  # Require authentication
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication


# Custom API View to update leaderboard entries
class UpdateLeaderboardView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication

    def post(self, request, *args, **kwargs):
        leaderboard_entries = LeaderboardEntry.objects.all()

        for entry in leaderboard_entries:
            entry.update_total_score()

        serializer = LeaderboardEntrySerializer(leaderboard_entries, many=True)
        return Response(serializer.data)
