from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Grade, Attendance, Course, Teacher

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'index_number']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
