from django.shortcuts import render
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from .models import Questions,Tag
from .serializers import QuestionsSerializer,TagSerializer

from .permissions import IsTeacher, IsStudent
class TeacherQuestionsListView(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = [IsTeacher]

    def get_queryset(self):
        """
        Returns questions created by the teacher specified in the URL.
        """
        teacher_id = self.kwargs.get('teacher_id')
        return Questions.objects.filter(created_by__id=teacher_id)
    
class AllQuestionsListView(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    permission_classes=[IsTeacher]

    def get_queryset(self):
        """
        Returns all questions.
        """
        return Questions.objects.all()    

class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionsSerializer
    permission_classes=[IsTeacher]

class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes=[IsTeacher]

class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer   
    permission_classes=[IsTeacher]
    
# List all tags or create a new tag
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes=[IsTeacher]

# Retrieve, update or delete a specific tag
class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer     
    permission_classes=[IsTeacher]
