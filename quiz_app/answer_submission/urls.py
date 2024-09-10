from django.urls import path
from .views import StudentsByQuizView, AnswerSubmissionListCreateView, AnswerSubmissionDetailView

urlpatterns = [
    path('quizzes/<int:quiz_id>/students/', StudentsByQuizView.as_view(), name='students-by-quiz'),
    path('answer-submissions/', AnswerSubmissionListCreateView.as_view(), name='answer-submission-list-create'),
    path('answer-submissions/<int:pk>/', AnswerSubmissionDetailView.as_view(), name='answer-submission-detail'),
]

