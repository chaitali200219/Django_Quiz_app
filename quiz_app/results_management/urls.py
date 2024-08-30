# results_management/urls.py

from django.urls import path
from .views import (
    QuizResultListView, QuizResultDetailView,
    QuestionResultListView, QuestionResultDetailView,
    LeaderboardEntryListView, UpdateLeaderboardView
)

urlpatterns = [
    # Quiz Results URLs
    path('quiz-results/', QuizResultListView.as_view(), name='quiz-result-list'),
    path('quiz-results/<int:pk>/', QuizResultDetailView.as_view(), name='quiz-result-detail'),

    # Question Results URLs
    path('question-results/', QuestionResultListView.as_view(), name='question-result-list'),
    path('question-results/<int:pk>/', QuestionResultDetailView.as_view(), name='question-result-detail'),

    # Leaderboard URLs
    path('leaderboard/', LeaderboardEntryListView.as_view(), name='leaderboard-list'),
    path('leaderboard/update/', UpdateLeaderboardView.as_view(), name='update-leaderboard'),
]
