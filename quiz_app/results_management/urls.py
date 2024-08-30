from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<int:quiz_id>/results/', views.calculate_results, name='calculate_results'),
]
