from rest_framework import generics
from .models import AnswerSubmission
from .serializers import QuizSubmissionSerializer
from django.db.models import Count

class QuizSubmissionView(generics.ListAPIView):
    serializer_class = QuizSubmissionSerializer

    def get_queryset(self):
        quiz_id = self.kwargs.get('quiz_id')
        if not quiz_id:
            return AnswerSubmission.objects.none()
        
        # Get all submissions for the quiz and annotate them to ensure distinct students
        return AnswerSubmission.objects.filter(quiz_id=quiz_id).values('student').annotate(count=Count('student')).filter(count__gt=0)
