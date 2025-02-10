from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Grade, Attendance
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, StudentForm, GradeForm, AttendanceForm, CourseForm, TeacherForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Profile, Student, Grade, Attendance, Course, Teacher

# Create your views here.

def welcome(request):
    return render(request, 'school_management/welcome.html')

def login_view(request, user_type=None):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    if user_type == 'student':
        return render(request, 'school_management/login_student.html', context)
    elif user_type == 'teacher':
        return render(request, 'school_management/login_teacher.html', context)
    elif user_type == 'administrator':
        return render(request, 'school_management/login_administrator.html', context)
    else:
        return render(request, 'school_management/login.html', context)

def login_administrator(request):
    return login_view(request, 'administrator')

def login_teacher(request):
    return login_view(request, 'teacher')

def login_student(request):
    return login_view(request, 'student')

@login_required
def dashboard(request):
    return render(request, 'school_management/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            Profile.objects.create(user=user, user_type='student')
            user_type=request.POST.get('user_type')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'school_management/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# Student views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'school_management/student_list.html', {'students': students})

@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'school_management/add_student.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'school_management/student_update.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'school_management/student_delete.html', {'student': student})

# Grade views
def grade_list(request):
    students = Student.objects.all()
    grades = Grade.objects.all()
    student_grades = zip(students, grades)
    return render(request, 'school_management/grade_list.html', {'student_grades': student_grades})

@login_required
def add_grade(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.user = request.user
            grade.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'school_management/add_grade.html', {'form': form})

@login_required
def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            grade = form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'school_management/grade_update.html', {'form': form})

@login_required
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == "POST":
        grade.delete()
        return redirect('grade_list')
    return render(request, 'school_management/grade_delete.html', {'grade': grade})

# Course views
def courses_list(request):
    courses = Course.objects.all()
    teacher = Teacher.objects.all()
    course_teacher = zip(courses, teacher)
    return render(request, 'school_management/courses_list.html', {'course_teacher': course_teacher})

@login_required
def add_courses(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect('courses_list')
    else:
        form = CourseForm()
    return render(request, 'school_management/add_courses.html', {'form': form})

@login_required
def courses_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('courses_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'school_management/courses_update.html', {'form': form})

@login_required
def courses_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect('courses_list')
    return render(request, 'school_management/courses_delete.html', {'course': course})

# Attendance views
def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'school_management/attendance_list.html', {'attendance_records': attendance_records})

@login_required
def add_attendance(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.user = request.user
            attendance.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'school_management/add_attendance.html', {'form': form})

@login_required
def attendance_update(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            attendance = form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'school_management/attendance_update.html', {'form': form})

@login_required
def attendance_delete(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == "POST":
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'school_management/attendance_delete.html', {'attendance': attendance})


# Teacher views
@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school_management/.html', {'teachers': teachers})

@login_required
def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = request.user
            teacher.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'school_management/add_teacher.html', {'form': form})

@login_required
def teacher_update(request):
    teacher = request.user.teacher
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            teacher = form.save()
            return redirect('teacher_profile')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'school_management/teacher_update.html', {'form': form})

@login_required
def teacher_delete(request):
    teacher = request.user.teacher
    if request.method == "POST":
        teacher.delete()
        return redirect('teacher_profile')
    return render(request, 'school_management/teacher_delete.html', {'teacher': teacher})
