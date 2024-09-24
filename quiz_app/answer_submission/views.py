from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import AnswerSubmission, Questions
from .serializers import AnswerSubmissionSerializer, QuizSerializer
from quiz_management.permissions import IsTeacher,IsStudent
from quiz_management.models import Quiz



class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsStudent | IsTeacher]


    def get_queryset(self):
        """
        Returns all quizzes.
        """
        return Quiz.objects.all()
    
    def get_serializer_context(self):
        # Pass the request context to the serializer, so it can access the user
        return {'request': self.request}
    
    

# View to get submissions by quiz
class StudentsByQuizView(APIView):
    def get(self, request, quiz_id, *args, **kwargs):
        submissions = AnswerSubmission.objects.filter(quiz_id=quiz_id).select_related('student', 'quiz')
        serializer = AnswerSubmissionSerializer(submissions, many=True)
        return Response(serializer.data)
    



# View for listing and creating answer submissions
class AnswerSubmissionListCreateView(generics.ListCreateAPIView):
    queryset = AnswerSubmission.objects.all()
    serializer_class = AnswerSubmissionSerializer

    def perform_create(self, serializer):
        # Automatically set the student_id from the request
        serializer.save(student_id=self.request.data.get('student_id'))
        
# View for retrieving, updating, and deleting a specific answer submission
class AnswerSubmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerSubmission.objects.all()
    serializer_class = AnswerSubmissionSerializer
    
    

