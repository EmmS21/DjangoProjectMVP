from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, TemplateView)

from ..decorators import teacher_required
from ..forms import TeacherSignUpForm, MentorPaymentForm, UserForm
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from ..decorators import student_required,check_is_allow
from ..forms import *
from ..models import Quiz, Student, TakenQuiz, Mentor
from django.http import HttpResponseRedirect
import json

from django.contrib.auth import get_user_model
User = get_user_model()


#not useable
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        username = form.cleaned_data.get('first_name')
        email = form.cleaned_data.get('email')
        htmly = get_template('classroom/teachers/email.html')
        d = {'username': username}
        subject, from_email, to = 'Welcome to GradientBoost', 'emmanuel@thegradientboost.com', email
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        if self.request.user.is_activated:
            return redirect('teachers:app-instructor-dashboard')
        return redirect('notyet')

# edit mentor profile
@login_required
@teacher_required
@check_is_allow
def edit_user(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        # mentorform = MentorProfileForm(request.POST, request.FILES, instance=user.mentor)
        if form.is_valid():
            # m = Mentor.objects.get()
            form.save()
            # m.photo = mentorform.cleaned_data['photo']
            # m.save()
            messages.success(request, f'Your profile was successfully updated!')
            return HttpResponseRedirect('%s' % (reverse('teachers:edit_user')))
        # else:
        #     messages.error(request, ('Please correct the error below.'))
    else:
        form = UserForm(instance=user)
    return render(request, 'classroom/teachers/app-instructor-profile.html', {'form': form})


# custom logout redirect
@method_decorator([login_required, teacher_required, check_is_allow], name='dispatch')
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully been logged out")
    return redirect('teachers:app-student-dashboard')

#course details
def course_details(request):
    return render(request, 'classroom/teachers/app-take-course.html')


# #edit profile page
# @method_decorator([login_required, teacher_required], name='dispatch')
# def editmenprofile(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect('teachers:app-instructor-profile')
#     else:
#         form = UserChangeForm(instance=request.user)
#         args = {'form':form}
#         return render(request, 'teachers:add-instructor-dashboard')

@method_decorator([login_required, teacher_required, check_is_allow], name='dispatch')
class QuizListView(ListView):
    model = Quiz
    ordering = ('name',)
    context_object_name = 'quizzes'
    template_name = 'classroom/teachers/app-instructor-dashboard.html'

    def get_queryset(self):
        queryset = self.request.user.quizzes \
            .select_related('subject') \
            .annotate(questions_count=Count('questions', distinct=True)) \
            .annotate(taken_count=Count('taken_quizzes', distinct=True))
        return queryset

# @method_decorator([login_required, teacher_required], name='dispatch')
@login_required
@teacher_required
@check_is_allow
def statement(request):
    return render(request, 'classroom/teachers/app-instructor-statement.html')

# @method_decorator([login_required, teacher_required], name='dispatch')
@login_required
@teacher_required
@check_is_allow
def mentor_messages(request):
    return render(request, 'classroom/teachers/app-instructor-messages.html')

#get list of students
@login_required
@teacher_required
@check_is_allow
def student_list(request):
    students = User.objects.filter(is_student=True)
    template_name = 'classroom/teachers/student_list.html'
    context = {'students': students}
    return render(request, template_name, context)

@login_required
@teacher_required
@check_is_allow
def payment_view(request):
    form = MentorPaymentForm()
    if request.method == 'POST':
        form = MentorPaymentForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.mentor.branch_code = form.cleaned_data['branch_code']
            user.mentor.address = form.cleaned_data['address']
            user.mentor.account_num = form.cleaned_data['account_num']
            user.mentor.branch_code = form.cleaned_data['branch_code']
            user.mentor.bank_name = form.cleaned_data['bank_name']
            user.mentor.billing_name = form.cleaned_data['billing_name']
            user.save()
            user.mentor.save()
            return redirect('teachers:payment_view')
    else:
        form = MentorPaymentForm(instance=request.user)
    return render(request, 'classroom/teachers/app-instructor-billing.html', {'form': form})

@login_required
@teacher_required
@check_is_allow
def take_course(request):
    return render(request, 'classroom/teachers/app-take-course.html')
