# results_management/urls.py

from django.urls import path
from .views import (
    QuizResultListView,
    QuizResultDetailView,
    LeaderboardEntryListView,
    SubmitQuizView,
    UpdateLeaderboardView
)

urlpatterns = [
    path('quiz-results/', QuizResultListView.as_view(), name='quiz-result-list'),
    path('quiz-results/<int:pk>/', QuizResultDetailView.as_view(), name='quiz-result-detail'),
    path('leaderboard/', LeaderboardEntryListView.as_view(), name='leaderboard-entry-list'),
    path('submit-quiz/', SubmitQuizView.as_view(), name='submit-quiz'),
    path('update-leaderboard/', UpdateLeaderboardView.as_view(), name='update-leaderboard'),
]
