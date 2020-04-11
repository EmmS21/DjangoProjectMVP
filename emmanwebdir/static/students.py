from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ..decorators import student_required, check_is_allow
from ..forms import *
from ..models import Quiz, Student, TakenQuiz, Mentor
from django.http import HttpResponseRedirect
import json

from django.contrib.auth import get_user_model
User = get_user_model()

#dashboard
# @method_decorator([login_required, student_required], name='dispatch')
@login_required
@student_required
@check_is_allow
def dashboard(request):
    # if request.user.is_allow:
    return render(request,'classroom/students/app-student-dashboard.html')
    # else:
        # messages.warning(request, 'You account is not approved from admin yet')
        # return redirect('home')
#directory grid
# @method_decorator([login_required, student_required], name='dispatch')
@login_required
@student_required
@check_is_allow
def directory_grid(request):
    return render(request,'classroom/students/app-directory-grid.html')

        
#course page
# @method_decorator([login_required, student_required], name='dispatch')
@login_required
@student_required
@check_is_allow
def take_course(request):
    return render(request, 'classroom/students/app-take-course.html')

#edit student profile page
@login_required
@student_required
@check_is_allow
def edit_user(request):
    user = request.user
    if request.method == 'POST':
        form = StudentUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('%s' % (reverse('students:edit_user')))
    else:
        form = StudentUserForm(instance=user)
    return render(request, 'classroom/students/app-student-profile.html', {'form': form})

#get list of mentors
@login_required
@student_required
@check_is_allow
def mentor_list(request):
    mentors = User.objects.filter(is_teacher=True).select_related('mentor')
    for user in mentors:
        try:
            print(user.mentor.linkedin)
        except:
            pass
    # for user in mentors:
    #     print(user.linkedin)
    template_name = 'classroom/students/mentor_list.html'
    context = {'mentors': mentors}
    return render(request, template_name, context)

#learning material
@login_required
@student_required
@check_is_allow
def what_is_ml(request):
    return render(request, 'classroom/students/what_is_machine_learning.html')

@login_required
@student_required
@check_is_allow
def end_to_end(request):
    return render(request, 'classroom/students/building_end_to_end.html')

@login_required
@student_required
@check_is_allow
def linear_reg(request):
    return render(request, 'classroom/students/Linear_Regression.html')

@login_required
@student_required
@check_is_allow
def logistic_reg(request):
    return render(request, 'classroom/students/logistic_regression.html')

@login_required
@student_required
@check_is_allow
def logistic_reg_example(request):
    return render(request, 'classroom/students/log_reg.html')

@login_required
@student_required
@check_is_allow
def knearest(request):
    return render(request, 'classroom/students/knearest.html')

@login_required
@student_required
@check_is_allow
def k_nearest_practical(request):
    return render(request, 'classroom/students/knearestneighbors.html')

@login_required
@student_required
@check_is_allow
def decision_tree(request):
    return render(request, 'classroom/students/decisiontree.html')


@method_decorator([login_required, student_required, check_is_allow], name='dispatch')
class TakenQuizListView(ListView):
    model = TakenQuiz
    context_object_name = 'taken_quizzes'
    template_name = 'classroom/students/taken_quiz_list.html'

    def get_queryset(self):
        queryset = self.request.user.student.taken_quizzes \
            .select_related('quiz', 'quiz__subject') \
            .order_by('quiz__name')
        return queryset


@login_required
def take_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    student = request.user.student

    if student.quizzes.filter(pk=pk).exists():
        return render(request, 'students/taken_quiz.html')

    total_questions = quiz.questions.count()
    unanswered_questions = student.get_unanswered_questions(quiz)
    total_unanswered_questions = unanswered_questions.count()
    progress = 100 - round(((total_unanswered_questions - 1) / total_questions) * 100)
    question = unanswered_questions.first()

    if request.method == 'POST':
        form = TakeQuizForm(question=question, data=request.POST)
        if form.is_valid():
            with transaction.atomic():
                student_answer = form.save(commit=False)
                student_answer.student = student
                student_answer.save()
                if student.get_unanswered_questions(quiz).exists():
                    return redirect('students:take_quiz', pk)
                else:
                    correct_answers = student.quiz_answers.filter(answer__question__quiz=quiz, answer__is_correct=True).count()
                    score = round((correct_answers / total_questions) * 100.0, 2)
                    TakenQuiz.objects.create(student=student, quiz=quiz, score=score)
                    if score < 50.0:
                        messages.warning(request, f'Better luck next time! Your score for the quiz %s was {(quiz.name, score)}')
                    else:
                        messages.success(request, 'Congratulations! You completed the quiz %s with success! You scored {(quiz.name, score)} points.')
                    return redirect('students:quiz_list')
    else:
        form = TakeQuizForm(question=question)

    return render(request, 'classroom/students/take_quiz_form.html', {
        'quiz': quiz,
        'question': question,
        'form': form,
        'progress': progress
    })
