from rest_framework import serializers
from .models import AnswerSubmission
from user_management.models import Student
from question_management.models import Questions, Option
from quiz_management.models import Quiz

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'content']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)  # Include options for each question

    class Meta:
        model = Questions
        fields = ['id', 'content', 'options']


class QuizSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    questions = QuestionSerializer(many=True)  # Include related questions

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'duration', 'status', 'questions']

    def get_status(self, obj):
        # Get the current user (student) from the request context
        user = self.context['request'].user

        try:
            student = user.student
        except Student.DoesNotExist:
            return "No Student Profile"

        # Check if there are any answer submissions for this quiz by this student
        submission = AnswerSubmission.objects.filter(quiz=obj, student=student).first()

        if not submission:
            return "Not Started"
        elif submission.status == 'pending':
            return "In Progress"
        elif submission.status == 'submitted':
            return "Completed"
        return "Unknown"


class AnswerSubmissionSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = AnswerSubmission
        fields = ['quiz', 'question', 'option', 'student_id', 'is_correct', 'status']

    def create(self, validated_data):
        student_id = validated_data.pop('student_id')
        student = Student.objects.get(id=student_id)
        validated_data['student'] = student
        return super().create(validated_data)