from django.shortcuts import redirect, render

#redirects after signup
def home(request):
    if request.user.is_authenticated and request.user.is_allow:
        if request.user.is_teacher:
            return redirect('teachers:app-instructor-dashboard')
        elif request.user.is_student:
            return redirect('students:app-student-dashboard')
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

