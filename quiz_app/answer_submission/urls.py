from django.urls import path
from .views import QuizSubmissionView

urlpatterns = [
    path('answer_submissions/<int:quiz_id>/', QuizSubmissionView.as_view(), name='answer_submissions'),
]
