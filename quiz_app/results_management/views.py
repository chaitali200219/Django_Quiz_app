# results_management/views.py

from rest_framework import generics
from .models import QuizResult, QuestionResult, LeaderboardEntry
from .serializers import QuizResultSerializer, QuestionResultSerializer, LeaderboardEntrySerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

# View to list all quiz results or create a new quiz result
class QuizResultListView(generics.ListCreateAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer


# View to retrieve, update, or delete a specific quiz result
class QuizResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer


# View to list all question results or create a new question result
class QuestionResultListView(generics.ListCreateAPIView):
    queryset = QuestionResult.objects.all()
    serializer_class = QuestionResultSerializer


# View to retrieve, update, or delete a specific question result
class QuestionResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionResult.objects.all()
    serializer_class = QuestionResultSerializer


# View to list leaderboard entries or create a new leaderboard entry
class LeaderboardEntryListView(generics.ListAPIView):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer


# Custom API View to update leaderboard entries
class UpdateLeaderboardView(APIView):
    def post(self, request, *args, **kwargs):
        # Logic to update the leaderboard
        leaderboard_entries = LeaderboardEntry.objects.all()
        # Logic to recalculate total scores and update leaderboard
        for entry in leaderboard_entries:
            total_score = QuizResult.objects.filter(student=entry.student).aggregate(models.Sum('score'))['score__sum'] or 0
            entry.total_score = total_score
            entry.save()

        serializer = LeaderboardEntrySerializer(leaderboard_entries, many=True)
        return Response(serializer.data)
