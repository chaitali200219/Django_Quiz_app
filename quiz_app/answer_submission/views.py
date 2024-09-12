from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import AnswerSubmission, Questions
from .serializers import AnswerSubmissionSerializer

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question']  # Allows filtering by question_id

    def perform_create(self, serializer):
        serializer.save()

# View for retrieving, updating, and deleting a specific answer submission
class AnswerSubmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSubmissionSerializer

    # Dynamically filter the queryset based on student_id
    def get_queryset(self):
        pk = self.kwargs.get('pk')  # Get the primary key from the URL
        return AnswerSubmission.objects.filter(pk=pk)
