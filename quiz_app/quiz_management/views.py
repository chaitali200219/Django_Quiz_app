from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer
from .permissions import IsTeacher,IsStudent

class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsStudent | IsTeacher]


    def get_queryset(self):
        """
        Returns all quizzes.
        """
        return Quiz.objects.all()

class QuizCreateView(generics.CreateAPIView):
    
    serializer_class = QuizSerializer
    permission_classes=[IsTeacher]

class QuizUpdateView(generics.UpdateAPIView):
    permission_classes=[IsAdminOrTeacher]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes=[IsTeacher]
    

class QuizDeleteView(generics.DestroyAPIView):
    permission_classes=[IsAdminOrTeacher]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes=[IsTeacher]


