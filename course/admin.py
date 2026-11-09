from django.contrib import admin
from .models import Student, Teacher, Subject

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sertifikat')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'student')
