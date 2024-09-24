from django.urls import path

from .import views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import StudentListView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     # Teacher Registration
    path('api/register/teacher/', views.TeacherRegisterView.as_view(), name='teacher_register'),
    
    
    
    # Student Registration
    path('api/register/student/', views.StudentRegisterView.as_view(), name='student_register'),
    
    path('api/login/', views.LoginView.as_view(), name='login'),
    
    # Logout (common for both teachers and students)
    path('api/logout/', views.LogoutView.as_view(), name='logout'),
    
    
    path('students/id/<str:username>/', views.get_student_id, name='get_student_id'),#new
    path('students/', StudentListView.as_view(), name='student-list'),
    

]