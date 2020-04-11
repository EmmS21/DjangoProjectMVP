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
        path('decision_tree_from_scratch', students.decision_tree_from_scratch, name='decision_tree_from_scratch'),
        path('descriptive_stats', students.descriptive, name='descriptive_stats'),
        path('descriptive_two', students.descript_stats, name='descriptive_two'),
        path('probability_one', students.proba_one, name='probability_one'),
        path('probability_one_exercises', students.proba_one_exercises, name='probability_one_exercises'),
        path('probability_exercises_two', students.proba_two_exercises, name='probability_exercises_two'),
        path('monty_hall', students.monty_hall, name='monty_hall'),
        path('probability_two', students.proba_two, name='probability_two'),
        path('probability_exercises_three', students.proba_three_exercises, name='probability_exercises_three'),
        path('bayesian_theory', students.bayesian_theory, name='bayesian_theory'),
        path('bayesian_exercises', students.bayesian_exercises, name='bayesian_exercises'),
        path('central_limit_theorem', students.central_limit_theorem, name='central_limit_theorem'),
        path('inferential_statistics', students.inferential_stats, name='inferential_statistics'),
        path('what_is_python_expressions.html', students.python_expressions, name='what_is_python_expressions.html'),
        path('control_flow_and_conditionals', students.control_flow_and_conditionals, name='control_flow_and_conditionals'),
        path('opening_and_reading', students.opening_and_reading, name='opening_and_reading'),
        path('pandas_one', students.pandas_one, name='pandas_one'),
        path('pandas_two', students.pandas_two, name='pandas_two'),
        path('object_oriented_programming', students.object_oriented_programming, name='object_oriented_programming'),
        ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.QuizListView.as_view(), name='app-instructor-dashboard'),
        path('edit_user', teachers.edit_user, name='edit_user'),
        path('mentor_messages', teachers.mentor_messages, name='mentor_messages'),
        path('statement', teachers.statement, name='app-instructor-statement'),
        path('course_details', teachers.course_details, name='app-take-course'),
        path('students', teachers.student_list, name='students'),
        path('take_course', teachers.take_course, name='app-take-course'),
        path('payment_view', teachers.payment_view, name='payment_view'),
        ], 'classroom'), namespace='teachers')),
]


