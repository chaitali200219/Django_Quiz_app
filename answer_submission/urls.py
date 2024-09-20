from django.urls import path
from .views import StudentsByQuizView, AnswerSubmissionListCreateView, AnswerSubmissionDetailView, QuizListView, QuizDetailView

urlpatterns = [
    path('quizzes/<int:quiz_id>/students/', StudentsByQuizView.as_view(), name='students-by-quiz'),
    path('answer-submissions/', AnswerSubmissionListCreateView.as_view(), name='answer-submission-list-create'),
    path('answer-submissions/<int:pk>/', AnswerSubmissionDetailView.as_view(), name='answer-submission-detail'),
    path('quizzes/', QuizListView.as_view(), name='quiz-list'),  # New URL pattern
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),
]

