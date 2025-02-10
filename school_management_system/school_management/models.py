from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    USER_TYPES = (
        ('administrator', 'Administrator'),
        ('teacher', 'teacher'),
        ('student', 'student'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    index_number = models.CharField(max_length=10, unique=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.subject} - {self.grade}"

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', related_name='courses_taught', on_delete=models.CASCADE)



    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
