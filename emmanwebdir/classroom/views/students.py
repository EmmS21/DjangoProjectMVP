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


# class StudentSignUpView(CreateView):
    # model = User
    # form_class = StudentSignUpForm
    # template_name = 'registration/signup_form.html'

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'student'
    #     return super().get_context_data(**kwargs)

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect('students:app-student-dashboard')

#logging out
# @method_decorator([login_required, student_required], name='dispatch')
# @login_required
# @student_required
# def logout_request(request):
#     logout(request)
#     messages.info(request, "You have successfully been logged out")
#     return redirect('student:app-student-dashboard')

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

#course material
@login_required
@student_required
def what_is_ml(request):
    return render(request, 'classroom/students/what_is_machine_learning.html')

@login_required
@student_required
def end_to_end(request):
    return render(request, 'classroom/students/building_end_to_end.html')

@login_required
@student_required
def linear_reg(request):
    return render(request, 'classroom/students/Linear_Regression.html')

@login_required
@student_required
def logistic_reg(request):
    return render(request, 'classroom/students/logistic_regression.html')

@login_required
@student_required
def logistic_reg_example(request):
    return render(request, 'classroom/students/log_reg.html')

@login_required
@student_required
def knearest(request):
    return render(request, 'classroom/students/knearest.html')

@login_required
@student_required
def k_nearest_practical(request):
    return render(request, 'classroom/students/knearestneighbors.html')

@login_required
@student_required
def decision_tree(request):
    return render(request, 'classroom/students/decisiontree.html')

@login_required
@student_required
def decision_tree_from_scratch(request):
    return render(request, 'classroom/students/decision_tree_from_scratch.html')


@login_required
@student_required
def descriptive(request):
    return render(request, 'classroom/students/descriptive_statistics.html')

@login_required
@student_required
def descript_stats(request):
    return render(request, 'classroom/students/descr_stats_graphs.html')

@login_required
@student_required
def proba_one(request):
    return render(request, 'classroom/students/probability_one.html')

@login_required
@student_required
def proba_one_exercises(request):
    return render(request, 'classroom/students/probability_one_exercises.html')

@login_required
@student_required
def proba_two_exercises(request):
    return render(request, 'classroom/students/probability_exercises_two.html')

@login_required
@student_required
def proba_two(request):
    return render(request, 'classroom/students/probability_two.html')

@login_required
@student_required
def monty_hall(request):
    return render(request, 'classroom/students/monty_hall.html')

@login_required
@student_required
def proba_three_exercises(request):
    return render(request, 'classroom/students/probability_exercises_three.html')

@login_required
@student_required
def bayesian_theory(request):
    return render(request, 'classroom/students/bayesian_theory.html')

@login_required
@student_required
def bayesian_exercises(request):
    return render(request, 'classroom/students/bayesian_exercises.html')

@login_required
@student_required
def central_limit_theorem(request):
    return render(request, 'classroom/students/central_limit_theorem.html')

@login_required
@student_required
def inferential_stats(request):
    return render(request, 'classroom/students/inferential_statistics.html')

@login_required
@student_required
def python_expressions(request):
    return render(request, 'classroom/students/what_is_python_expressions.html')

@login_required
@student_required
def control_flow_and_conditionals(request):
    return render(request, 'classroom/students/control_flow_and_conditionals.html')

@login_required
@student_required
def opening_and_reading(request):
    return render(request, 'classroom/students/opening_and_reading.html')

@login_required
@student_required
def pandas_one(request):
    return render(request, 'classroom/students/pandas_one.html')

@login_required
@student_required
def pandas_two(request):
    return render(request, 'classroom/students/pandas_two.html')

@login_required
@student_required
def object_oriented_programming(request):
    return render(request, 'classroom/students/object_oriented_programming.html')

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
