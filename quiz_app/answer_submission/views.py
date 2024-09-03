from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework.response import Response
from .models import AnswerSubmission,Questions
from .serializers import AnswerSubmissionSerializer


from django_filters.rest_framework import DjangoFilterBackend

class AnswerSubmissionListCreateView(generics.ListCreateAPIView):
    queryset = AnswerSubmission.objects.all()
    serializer_class = AnswerSubmissionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question']  # Allows filtering by question_id

    def get_serializer_context(self):
        context = super().get_serializer_context()
        question_id = self.request.data.get('question')
        if question_id:
            context['question'] = Questions.objects.get(id=question_id)
        return context

    def perform_create(self, serializer):
        serializer.save()
