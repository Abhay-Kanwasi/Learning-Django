from django.contrib import admin
from .models import Student, Faculty

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id','student_name', 'student_email', 'student_password','comment')

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'faculty_name', 'faculty_email', 'faculty_subjects', 'faculty_slogan')

admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty, FacultyAdmin)