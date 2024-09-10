from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Teacher, Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['experience_years']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['grade']
