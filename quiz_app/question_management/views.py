from django.shortcuts import render
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from .models import Questions
from .serializers import QuestionsSerializer

class TeacherQuestionsListView(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns questions created by the teacher specified in the URL.
        """
        teacher_id = self.kwargs.get('teacher_id')
        return Questions.objects.filter(created_by__id=teacher_id)
    
class AllQuestionsListView(generics.ListAPIView):
    serializer_class = QuestionsSerializer

    def get_queryset(self):
        """
        Returns all questions.
        """
        return Questions.objects.all()    

class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionsSerializer

class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer    
