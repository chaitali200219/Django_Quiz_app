from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AnswerSubmission
from .serializers import StudentSerializer

class StudentsByQuizView(APIView):
    def get(self, request, quiz_id, *args, **kwargs):
        # Filter AnswerSubmission based on quiz_id
        submissions = AnswerSubmission.objects.filter(quiz_id=quiz_id).select_related('student')
        students = {submission.student.id: submission.student for submission in submissions}
        student_list = list(students.values())
        serializer = StudentSerializer(student_list, many=True)
        return Response(serializer.data)