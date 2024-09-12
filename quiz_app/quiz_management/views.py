from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Quiz
<<<<<<< HEAD
from .serializers import QuizSerializer 
from user_management.permissions import IsStudentOrTeacher, IsAdminOrTeacher
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated


class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    
=======
from .serializers import QuizSerializer
from .permissions import IsTeacher,IsStudent

class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsStudent | IsTeacher]


>>>>>>> 0d6686cf2341ceb701c1b7bb99a1a021cfb328a7
    def get_queryset(self):
        """
        Returns all quizzes.
        """
        return Quiz.objects.all()

class QuizCreateView(generics.CreateAPIView):
    
    serializer_class = QuizSerializer
<<<<<<< HEAD
    permission_classes=[IsAdminOrTeacher]
    
=======
    permission_classes=[IsTeacher]
>>>>>>> 0d6686cf2341ceb701c1b7bb99a1a021cfb328a7

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


