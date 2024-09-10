# results_management/models.py

from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from quiz_management.models import Quiz
from user_management.models import Student
from question_management.models import Questions, Option
from answer_submission.models import AnswerSubmission  # Import AnswerSubmission model

class QuizResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField(default=0.0)  # Default score is set to 0
    date_taken = models.DateTimeField(auto_now_add=True)

    def calculate_score(self):
        submissions = AnswerSubmission.objects.filter(student=self.student, quiz=self.quiz, status='submitted')
        self.score = submissions.filter(is_correct=True).count()
        self.save()

    def __str__(self):
        return f"{self.student.user.username} - {self.quiz.title} - Score: {self.score}"

    class Meta:
        unique_together = ('student', 'quiz')
        verbose_name = 'Quiz Result'
        verbose_name_plural = 'Quiz Results'


class QuestionResult(models.Model):
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.CASCADE, related_name='question_results')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_results')
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='selected_results', null=True)
    is_correct = models.BooleanField(default=False)
    marks_obtained = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.selected_option:
            self.is_correct = self.selected_option.is_correct
            self.marks_obtained = self.question.marks if self.is_correct else 0
        else:
            self.is_correct = False
            self.marks_obtained = 0
        
        super().save(*args, **kwargs)
        self.quiz_result.calculate_score()

    def __str__(self):
        return f"{self.quiz_result.student.user.username} - {self.question.content} - Correct: {self.is_correct}"

    class Meta:
        unique_together = ('quiz_result', 'question')
        verbose_name = 'Question Result'
        verbose_name_plural = 'Question Results'


class LeaderboardEntry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='leaderboard_entries')
    total_score = models.FloatField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def update_total_score(self):
        self.total_score = QuizResult.objects.filter(student=self.student).aggregate(Sum('score'))['score__sum'] or 0.0
        self.save()

    def __str__(self):
        return f"{self.student.user.username} - Total Score: {self.total_score}"

    class Meta:
        ordering = ['-total_score']
        verbose_name = 'Leaderboard Entry'
        verbose_name_plural = 'Leaderboard Entries'


@receiver(post_save, sender=QuizResult)
def update_leaderboard(sender, instance, **kwargs):
    leaderboard_entry, created = LeaderboardEntry.objects.get_or_create(student=instance.student)
    leaderboard_entry.update_total_score()

@receiver(post_save, sender=AnswerSubmission)
def update_quiz_result(sender, instance, **kwargs):
    quiz_result, created = QuizResult.objects.get_or_create(student=instance.student, quiz=instance.quiz)
    quiz_result.calculate_score()
