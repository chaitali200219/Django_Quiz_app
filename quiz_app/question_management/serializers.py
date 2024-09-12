from rest_framework import serializers
from .models import Questions, Option, Tag

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'content', 'is_correct', 'status']

class QuestionsSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, required=False)  # Nested serializer for options
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, required=False)  # Assuming you pass tag IDs

    class Meta:
        model = Questions
        fields = ['id', 'content', 'question_type', 'marks', 'created_at', 'created_by', 'options', 'tags']

    def create(self, validated_data):
        options_data = validated_data.pop('options', [])
        tags_data = validated_data.pop('tags', [])
        question = super().create(validated_data)
       

        # Create options for the question
        for option_data in options_data:
            Option.objects.create(question=question, **option_data)

        # Assign tags based on keywords in the content
        keyword_to_tag_map = {
    'capital': 'Geography',
    'python': 'Programming',
    'history': 'History',
    'space': 'Astronomy',
    'planet': 'Astronomy'
    # Add more keywords and corresponding tags here
}

        for keyword, tag_name in keyword_to_tag_map.items():
            if keyword.lower() in question.content.lower():
                tag, created = Tag.objects.get_or_create(name=tag_name)
                question.tags.add(tag)

        return question

    def update(self, instance, validated_data):
        options_data = validated_data.pop('options', [])
        tags_data = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)

        # Update options
        existing_options = {option.id: option for option in instance.options.all()}
        for option_data in options_data:
            option_id = option_data.get('id')
            if option_id:
                option = existing_options.get(option_id)
                if option:
                    for attr, value in option_data.items():
                        setattr(option, attr, value)
                    option.save()
            else:
                Option.objects.create(question=instance, **option_data)

        # Update tags
        instance.tags.set(tags_data)

        return instance

# Serializer for Tags
class TagSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'description', 'questions']

        
