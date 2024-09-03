from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('results/', include('results_management.urls')),  # This includes all results_management URLs
    path('answer/', include('answer_submission.urls')),
    path('questions/', include('question_management.urls')),

    path('quiz/',include('quiz_management.urls')),
    path('user/',include('user_management.urls')),
    path('api-auth/',include('rest_framework.urls')),


]
