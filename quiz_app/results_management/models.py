from django.db import models
from django.utils import timezone
from quiz_management.models import Quiz
from user_management.models import Student
from question_management.models import Questions, Option

class QuizResult(models.Model):
    """
    Stores the overall result of a student's attempt at a quiz.
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.quiz.title} - Score: {self.score}"

    class Meta:
        unique_together = ('student', 'quiz')
        verbose_name = 'Quiz Result'
        verbose_name_plural = 'Quiz Results'


class QuestionResult(models.Model):
    """
    Stores the result of a student's answer to a specific question in a quiz.
    """
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.CASCADE, related_name='question_results')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_results')
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='selected_results', null=True)
    is_correct = models.BooleanField(default=False)
    marks_obtained = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        """
        Override the save method to calculate if the answer is correct and assign marks accordingly.
        """
        self.is_correct = self.selected_option.is_correct if self.selected_option else False
        self.marks_obtained = self.question.marks if self.is_correct else 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quiz_result.student.user.username} - {self.question.content} - Correct: {self.is_correct}"

    class Meta:
        unique_together = ('quiz_result', 'question')
        verbose_name = 'Question Result'
        verbose_name_plural = 'Question Results'


class LeaderboardEntry(models.Model):
    """
    Represents an entry on the leaderboard, tracking total scores for each student.
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='leaderboard_entries')
    total_score = models.FloatField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.username} - Total Score: {self.total_score}"

    class Meta:
        ordering = ['-total_score']  # Order leaderboard by total score descending
        verbose_name = 'Leaderboard Entry'
        verbose_name_plural = 'Leaderboard Entries'
