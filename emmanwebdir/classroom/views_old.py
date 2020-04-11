from django.shortcuts import redirect, render
from django.views.generic import TemplateView

#redirects after signup
def home(request):
    # if request.user.is_authenticated and request.user.is_activated:
    #     if request.user.is_teacher:
    #         return redirect('teachers:app-instructor-dashboard')
    #     elif request.user.is_student:
    #         return redirect('students:app-student-dashboard')
    return render(request, 'classroom/home.html')

#about us page
def about(request):
    return render(request, 'classroom/about-us.html')
#courses page
def courses(request):
    return render(request, 'classroom/courses.html')
#course details
def course_details(request):
    return render(request, 'classroom/course-details.html')
#not yet
def notyet(request):
    return render(request, 'classroom/notyet.html')


# allauth.account.views.SignupView
from allauth.account.views import SignupView
from .forms import TeacherSignUpForm, StudentSignUpForm

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
    success_url = None

    def get_context_data(self, **kwargs):
        ret = super(StudentRegistrationView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret
