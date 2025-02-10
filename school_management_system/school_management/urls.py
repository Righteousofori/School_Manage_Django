from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('login/administrator/', views.login_administrator, name='login_administrator'),
    path('login/teacher/', views.login_teacher, name='login_teacher'),
    path('login/student/', views.login_student, name='login_student'),

    path('student/', views.student_list, name='student_list'),
    path('student/add_student/', views.add_student, name='add_student'),
    path('student/delete/<int:pk>/', views.student_delete, name='delete_student'),
    path('student/update/<int:pk>/', views.student_update, name='student_update'),

    path('teacher/', views.teacher_list, name='teacher_list'),
    path('teacher/add_teacher/', views.add_teacher, name='add_teacher'),
    path('teacher/delete/<int:pk>/', views.teacher_delete, name='delete_teacher'),
    path('teacher/update/<int:pk>/', views.teacher_update, name='teacher_update'),

    path('grade/', views.grade_list, name='grade_list'),
    path('grade/add_grade/', views.add_grade, name='add_grade'),
    path('grade/delete/<int:pk>/', views.grade_delete, name='delete_grade'),
    path('grade/update/<int:pk>/', views.grade_update, name='grade_update'),

    path('courses/', views.courses_list, name='courses_list'),
    path('courses/add_courses/', views.add_courses, name='add_courses'),
    path('courses/delete/<int:pk>/', views.courses_delete, name='delete_courses'),
    path('courses/update/<int:pk>/', views.courses_update, name='courses_update'),

    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add_attendance/', views.add_attendance, name='add_attendance'),
    path('attendance/delete/<int:pk>/', views.attendance_delete, name='delete_attendance'),
    path('attendance/update/<int:pk>/', views.attendance_update, name='attendance_update'),

    path('logout/', views.logout_view, name='logout'),
]

