from rest_framework import serializers
from .models import Questions, Tag

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'content', 'question_type', 'marks', 'created_at', 'created_by']

    def create(self, validated_data):
        # Create the question first
        question = super().create(validated_data)

        # Keyword to Tag mapping
        keyword_to_tag_map = {
            'capital': 'Geography',
            'python': 'Programming',
            'history': 'History',
            # Add more keywords and corresponding tags here
        }

        # Assign tags based on keywords in the content
        for keyword, tag_name in keyword_to_tag_map.items():
            if keyword.lower() in question.content.lower():
                # Get or create the Tag object
                tag, created = Tag.objects.get_or_create(name=tag_name)
                # Assign the tag to the question
                question.tags.add(tag)

        return question

# Serializer for Tags
class TagSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'description', 'questions']
