from django.db import models
from quiz_management.models import Quiz
from user_management.models import Student
from question_management.models import Option

# Create your models here.

class AnswerSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='submissions')
    is_correct = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[('submitted', 'Submitted'), ('pending', 'Pending')], default='pending')

    def __str__(self):
        return f"{self.student} - {self.quiz} - {self.status}"

    class Meta:
        unique_together = ('quiz', 'student', 'option')
