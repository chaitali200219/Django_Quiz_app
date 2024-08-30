from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer

class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        """
        Returns all quizzes.
        """
        return Quiz.objects.all()

class QuizCreateView(generics.CreateAPIView):
    serializer_class = QuizSerializer

class QuizUpdateView(generics.UpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDeleteView(generics.DestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


# Create your views here.
