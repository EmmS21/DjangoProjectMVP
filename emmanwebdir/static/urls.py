from django.urls import include, path

from .views.classroom import * 
from .views import students, teachers


urlpatterns = [ 
    path('', home, name='home'),
    path('about', about, name='about'),
    path('courses', courses, name='courses'),
    path('course_details', course_details, name='course_details'),
    path('notyet', notyet, name='notyet'),

    path('students/', include(([
        path('', students.dashboard, name='quiz_list'),
        # path('logout', students.logout_request, name="logout"),
        path('dashboard', students.dashboard, name='app-student-dashboard'),
        path('directory_grid', students.directory_grid, name='app-directory-grid'),
        path('take_course', students.take_course, name='app-take-course'),
        path('edit_user', students.edit_user, name='edit_user'),
        path('mentors', students.mentor_list, name='mentors'),
        path('what_is_ml', students.what_is_ml, name='what_is_machine_learning'),
        path('end_to_end', students.end_to_end, name='building_end_to_end'),
        path('linear_reg', students.linear_reg, name='linear_regression'),
        path('logistic_reg', students.logistic_reg, name='logistic_regression'),
        path('log_reg', students.logistic_reg_example, name='log_reg'),
        path('knearest', students.knearest, name='knearest'),
        path('k_nearest_practical', students.k_nearest_practical, name='k_nearest_practical'),
        path('decision_tree', students.decision_tree, name='decision_tree'),
    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.QuizListView.as_view(), name='app-instructor-dashboard'),
        # path('logout', teachers.logout_request, name="logout"),
        path('edit_user', teachers.edit_user, name='edit_user'),
        path('mentor_messages', teachers.mentor_messages, name='mentor_messages'),
        path('statement', teachers.statement, name='app-instructor-statement'),
        path('course_details', teachers.course_details, name='app-take-course'),
        path('students', teachers.student_list, name='students'),
        path('take_course', teachers.take_course, name='app-take-course'),
        path('payment_view', teachers.payment_view, name='payment_view'),

    ], 'classroom'), namespace='teachers')),

]


