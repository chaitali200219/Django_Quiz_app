from rest_framework import serializers
from .models import AnswerSubmission
from question_management.models import Option, Questions

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'content', 'is_correct']

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
