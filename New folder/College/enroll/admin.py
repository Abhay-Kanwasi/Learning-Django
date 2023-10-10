from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id','student_name', 'student_email', 'student_password','comment')

admin.site.register(Student, StudentAdmin)