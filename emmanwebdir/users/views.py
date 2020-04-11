from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from classroom.forms import TeacherSignUpForm, StudentSignUpForm
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'signup_selection.html'


class TeacherRegistrationView(SignupView):
    template_name = 'teacher_signup.html'
    form_class = TeacherSignUpForm
    redirect_field_name = 'next'
    success_url = None

    def get_context_data(self, **kwargs):
        ret = super(TeacherRegistrationView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret

class StudentRegistrationView(SignupView):
    template_name = 'student_signup.html'
    form_class = StudentSignUpForm
    redirect_field_name = 'next'
    success_url = 'students:app-student-dashboard'

    def get_context_data(self, **kwargs):
        ret = super(StudentRegistrationView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret
