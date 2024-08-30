# results_management/models.py

from django.db import models
from django.contrib.auth.models import User
from quiz_management.models import Quiz
from question_management.models import Questions, Option
from user_management.models import Student

class QuizResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.quiz.title} - {self.score}"

class QuestionResult(models.Model):
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.CASCADE, related_name='question_results')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_results')
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='selected_results', null=True)
    is_correct = models.BooleanField(default=False)
    marks_obtained = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quiz_result.student.full_name} - {self.question.content} - {'Correct' if self.is_correct else 'Incorrect'}"
