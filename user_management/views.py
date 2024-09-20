from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TeacherSerializer, StudentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Teacher, Student
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import generics

#new
def get_student_id(request, username):
    try:
        # Get the student using the username
        student = Student.objects.get(user__username=username)
        return JsonResponse({'student_id': student.id})
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    

class TeacherRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        experience_years = request.data.get('experience_years')

        if not username or not password or not experience_years:
            return Response({"error": "Username, password, and experience years are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User with this username already exists."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=username, password=make_password(password))
        Teacher.objects.create(user=user, experience_years=experience_years)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class StudentRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        grade = request.data.get('grade')

        if not username or not password or not grade:
            return Response({"error": "Username, password, and grade are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User with this username already exists."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=username, password=make_password(password))
        Student.objects.create(user=user, grade=grade)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Invalid credentials."},
                            status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        
        # Check if the user is a teacher or a student and fetch the respective ID
        teacher_id = user.teacher.id if hasattr(user, 'teacher') else None
        student_id = user.student.id if hasattr(user, 'student') else None

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'teacher_id': teacher_id,
            'student_id': student_id
        }, status=status.HTTP_200_OK)
