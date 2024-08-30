from rest_framework import serializers
from user_management.models import Student
from .models import AnswerSubmission

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user', 'grade']

class QuizSubmissionSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

    class Meta:
        model = AnswerSubmission
        fields = ['quiz', 'students']

    def get_students(self, obj):
        # Get all distinct students who have submitted answers for the specific quiz
        student_ids = AnswerSubmission.objects.filter(quiz=obj.quiz).values_list('student', flat=True).distinct()
        students = Student.objects.filter(id__in=student_ids)
        return StudentSerializer(students, many=True).data
