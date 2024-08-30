from django.test import TestCase
from .models import QuizResult

class QuizResultModelTest(TestCase):
    def test_string_representation(self):
        result = QuizResult(score=85.0)
        self.assertEqual(str(result), "Student - Quiz Title - 85.0")
