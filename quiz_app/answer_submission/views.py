from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import AnswerSubmission
from .serializers import AnswerSubmissionSerializer, StudentSerializer
from question_management.models import Questions
from user_management.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class AnswerSubmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerSubmission.objects.all()
    serializer_class = AnswerSubmissionSerializer

# View to list and create AnswerSubmission entries
class AnswerSubmissionListCreateView(generics.ListCreateAPIView):
    queryset = AnswerSubmission.objects.all()
    serializer_class = AnswerSubmissionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question']  # Allows filtering by question_id

    def get_serializer_context(self):
        # Adding context with question information
        context = super().get_serializer_context()
        question_id = self.request.data.get('question')
        if question_id:
            context['question'] = get_object_or_404(Questions, id=question_id)
        return context

    def perform_create(self, serializer):
        # This ensures the AnswerSubmission is saved with the provided data
        serializer.save()

# View to retrieve all students who have submitted answers for a quiz
class StudentsByQuizView(APIView):
    def get(self, request, quiz_id, *args, **kwargs):
        # Fetch all AnswerSubmissions related to the specific quiz
        submissions = AnswerSubmission.objects.filter(quiz_id=quiz_id).select_related('student')
        student_ids = {submission.student.id for submission in submissions}
        students = Student.objects.filter(id__in=student_ids)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
