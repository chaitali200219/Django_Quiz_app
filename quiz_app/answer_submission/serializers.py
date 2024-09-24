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
        # Get the current user (student or teacher) from the request context
        user = self.context['request'].user

        # Check if the user is a student
        try:
            if hasattr(user, 'student'):
                profile = user.student
                submission = AnswerSubmission.objects.filter(quiz=obj, student=profile).first()
            # Check if the user is a teacher
            elif hasattr(user, 'teacher'):
                profile = user.teacher
                # Assuming the field 'teacher' exists in AnswerSubmission to record teacher submissions
                submission = AnswerSubmission.objects.filter(quiz=obj, teacher=profile).first()
            else:
                return "No Profile"

            # Determine the quiz status based on submission
            if not submission:
                return "Not Started"
            elif submission.status == 'pending':
                return "In Progress"
            elif submission.status == 'submitted':
                return "Completed"
            return "Unknown"
        
        except (Student.DoesNotExist, Teacher.DoesNotExist):
            return "No Profile"


class AnswerSubmissionSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(write_only=True, required=False)
    teacher_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = AnswerSubmission
        fields = ['quiz', 'question', 'option', 'student_id', 'teacher_id', 'is_correct', 'status']

    def create(self, validated_data):
        student_id = validated_data.pop('student_id', None)
        teacher_id = validated_data.pop('teacher_id', None)

        if student_id:
            profile = Student.objects.get(id=student_id)
            validated_data['student'] = profile
        elif teacher_id:
            profile = Teacher.objects.get(id=teacher_id)
            validated_data['teacher'] = profile
        else:
            raise serializers.ValidationError("Either student_id or teacher_id must be provided.")

        return super().create(validated_data)