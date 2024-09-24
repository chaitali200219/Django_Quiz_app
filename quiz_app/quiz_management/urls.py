from django.urls import path
from .views import QuizListView, QuizCreateView, QuizUpdateView, QuizDeleteView

urlpatterns = [
    path('quizzes/<int:teacher_id>/', QuizListView.as_view(), name='quiz-list'),
    path('quizzes/create/', QuizCreateView.as_view(), name='quiz-create'),
    path('quizzes/<int:pk>/update/', QuizUpdateView.as_view(), name='quiz-update'),
    path('quizzes/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz-delete'),
]
