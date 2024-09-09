from rest_framework import serializers
from .models import AnswerSubmission
from question_management.models import Option, Questions
from user_management.models import Student  # Assuming this is where the Student model is defined

# Serializer for the Option model
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'content', 'is_correct']

# Serializer for AnswerSubmission model
class AnswerSubmissionSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Questions.objects.all())
    options = serializers.SerializerMethodField()  # To dynamically get options based on question

    class Meta:
        model = AnswerSubmission
        fields = ['quiz', 'student', 'option', 'question', 'is_correct', 'status', 'options']

    def get_options(self, obj):
        # Filter and return options related to the specific question
        question = self.context.get('question') or obj.question
        options = Option.objects.filter(question=question)
        return OptionSerializer(options, many=True).data

# New StudentSerializer for Student data serialization
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'grade']  # Adjust the fields to match your Student model
