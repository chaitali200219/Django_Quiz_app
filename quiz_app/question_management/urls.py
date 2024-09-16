from django.urls import path
from .views import TeacherQuestionsListView,AllQuestionsListView,QuestionCreateView,QuestionDetailView,QuestionUpdateView,QuestionDeleteView,TagDetailView,TagListCreateView

urlpatterns = [
    # question urls
    path('teachers/<int:teacher_id>/questions/', TeacherQuestionsListView.as_view(), name='teacher-questions-list'),
    
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('teachers/allquestions/',AllQuestionsListView.as_view(),name="questions"),
    path('questions/create/', QuestionCreateView.as_view(), name='question-create'),
    path('questions/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    
    #tag urls
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
]
