from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import Teacher,Student
class IsAdminOrTeacher(BasePermission):
    """
    Custom permission to allow access to admins and teachers.
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        try:
            return request.user.teacher is not None
        except Teacher.DoesNotExist:
            return False

class IsStudentOrTeacher(BasePermission):
    """
    Custom permission to allow students and teachers to view and attempt quizzes.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        try:
            # Check if the user is a teacher or student
            return request.user.teacher is not None or request.user.student is not None
        except (Teacher.DoesNotExist, Student.DoesNotExist):
            return False
