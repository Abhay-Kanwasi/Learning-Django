from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=70)
    student_email = models.EmailField(max_length=70)
    student_password = models.CharField(max_length=70)
    comment = models.CharField(max_length=40, default='not available')

    def __str__(self):
        return self.student_name
    
class Faculty(models.Model):
    faculty_name = models.CharField(max_length=30)
    faculty_id = models.IntegerField()
    faculty_email = models.EmailField()
    faculty_subjects = models.TextField()
    faculty_slogan = models.TextField()

    def __str__(self):
        return self.faculty_name
    
class Staff(models.Model):
    staff_name = models.CharField(max_length=30)
    staff_id = models.IntegerField()
    staff_email = models.EmailField()
    staff_subjects = models.TextField()
    staff_slogan = models.TextField()

    def __str__(self):
        return self.staff_name