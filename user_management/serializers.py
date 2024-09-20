from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Teacher, Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['experience_years']

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)  # Assuming user is linked
   
    class Meta:
        model = Student
        fields = ('id', 'username','grade')