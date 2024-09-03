from django.db import models
from quiz_management.models import Quiz
from user_management.models import Student
from question_management.models import Option, Questions

class AnswerSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='submissions',default=1)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='submissions')
    
    is_correct = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[('submitted', 'Submitted'), ('pending', 'Pending')], default='pending')

    def save(self, *args, **kwargs):
        # Automatically set is_correct based on the linked option
        self.is_correct = self.option.is_correct
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.quiz} - {self.question} - {self.status} - Correct: {self.is_correct}"

    class Meta:
        unique_together = ('quiz', 'student', 'option')
