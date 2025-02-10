from django.contrib import admin
from .models import Student, Grade, Attendance, Course, Teacher


# Register your models here.

admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Attendance)
admin.site.register(Course)
admin.site.register(Teacher)
