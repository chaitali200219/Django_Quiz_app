from django.urls import path
from .views import TeacherQuestionsListView,AllQuestionsListView,QuestionCreateView,QuestionUpdateView,QuestionDeleteView

urlpatterns = [
    path('teachers/<int:teacher_id>/questions/', TeacherQuestionsListView.as_view(), name='teacher-questions-list'),
    path('teachers/allquestions/',AllQuestionsListView.as_view(),name="questions"),
    path('questions/create/', QuestionCreateView.as_view(), name='question-create'),
    path('questions/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
]
