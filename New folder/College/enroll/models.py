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