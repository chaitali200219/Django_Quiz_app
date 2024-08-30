from django.urls import path
from .views import StudentsByQuizView

urlpatterns = [
    path('quizzes/<int:quiz_id>/students/', StudentsByQuizView.as_view(), name='students-by-quiz'),
]
