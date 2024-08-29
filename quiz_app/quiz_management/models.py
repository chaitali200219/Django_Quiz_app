from django.db import models
from question_management.models import Questions
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Quiz(models.Model):
    STATUS_CHOICES = [
        (True, _('Active')),
        (False, _('Inactive')),
    ]

    title = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()

    status = models.BooleanField(choices=STATUS_CHOICES, default=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    # Linking Quiz to Questions
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="quiz")

    def __str__(self):
        return self.title

    def clean(self):
        # Custom validation for the duration field
        if not (5 <= self.duration <= 15):
            raise ValidationError(_('Duration must be between 5 and 15 minutes.'))

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")






# Create your models here.
