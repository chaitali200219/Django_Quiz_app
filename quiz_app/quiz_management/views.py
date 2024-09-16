from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer
from .permissions import IsTeacher,IsStudent
from user_management.models import Teacher
from rest_framework.exceptions import ValidationError

class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsStudent | IsTeacher]

    def get_queryset(self):
        """
        Returns quizzes filtered by teacher ID or all active quizzes for students.
        """
        user = self.request.user
        teacher_id = self.kwargs.get('teacher_id')
        status = self.request.query_params.get('status')

        if teacher_id:
            # Filter by the given teacher_id
            teacher = get_object_or_404(Teacher, id=teacher_id)
            queryset = Quiz.objects.filter(created_by=teacher)
        else:
            # For students, return all active quizzes
            queryset = Quiz.objects.filter(status=True)

        # If the user is a teacher, return quizzes they created
        if hasattr(user, 'teacher'):
            return queryset
        else:
            return queryset

    def get(self, request, *args, **kwargs):
        """
        Overriding the get method to ensure that users are filtered correctly
        based on their roles and teacher ID.
        """
        if hasattr(request.user, 'teacher'):
            return self.list(request, *args, **kwargs)
        else:
            # For students, make sure they can only see active quizzes
            queryset = self.get_queryset()
            return self.list(request, *args, **kwargs)

class QuizCreateView(generics.CreateAPIView):
    
    serializer_class = QuizSerializer
    permission_classes=[IsTeacher]
    
    def perform_create(self, serializer):
        user = self.request.user
        try:
            # Get the Teacher instance related to this user
            teacher = Teacher.objects.get(user=user)
        except Teacher.DoesNotExist:
            raise ValidationError("The authenticated user is not a registered teacher.")
        
        # Save the quiz with the current teacher as the creator
        serializer.save(created_by=teacher)

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


