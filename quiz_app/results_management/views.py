from django.shortcuts import render, get_object_or_404
from .models import Quiz, QuizResult, LeaderboardEntry
from django.contrib.auth.decorators import login_required

@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    result = QuizResult.objects.filter(quiz=quiz, user=request.user).first()
    return render(request, 'results_management/quiz_result.html', {'quiz': quiz, 'result': result})

@login_required
def leaderboard(request):
    leaderboard_entries = LeaderboardEntry.objects.order_by('-total_score')
    return render(request, 'results_management/leaderboard.html', {'leaderboard_entries': leaderboard_entries})
# results_management/views.py

from django.shortcuts import render, get_object_or_404
from .models import QuizResult, QuestionResult
from quiz_management.models import Quiz
from question_management.models import Questions, Option
from user_management.models import Student

def calculate_results(request, quiz_id):
    # Fetch the quiz
    quiz = get_object_or_404(Quiz, id=quiz_id)

    # Example of calculating results
    if request.method == "POST":
        student = request.user.student  # Assuming `Student` model has a OneToOne with User
        quiz_result = QuizResult.objects.create(student=student, quiz=quiz, score=0)

        total_score = 0
        for question in quiz.questions_set.all():
            selected_option_id = request.POST.get(f"question_{question.id}")
            selected_option = Option.objects.get(id=selected_option_id)

            is_correct = selected_option.is_correct
            marks_obtained = question.marks if is_correct else 0
            total_score += marks_obtained

            # Save the question result
            QuestionResult.objects.create(
                quiz_result=quiz_result,
                question=question,
                selected_option=selected_option,
                is_correct=is_correct,
                marks_obtained=marks_obtained,
            )

        # Update the total score for the quiz
        quiz_result.score = total_score
        quiz_result.save()

        # Render a template to show the result
        return render(request, 'results_management/quiz_result.html', {'quiz_result': quiz_result})

    return render(request, 'results_management/quiz_start.html', {'quiz': quiz})
