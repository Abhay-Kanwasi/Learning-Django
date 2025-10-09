"""
Model Relationships

Django offers way to define the 3 most common types of database relationships.
"""

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.CharField(max_length=25)
    quantity = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    is_available = models.CharField(max_length=25)

class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(max_length=25)

# Create table called <app-name>_student
# Add columns : id, name,
# Example: student1 = Student(name='Abhay', age=24)
# student1.save() # Inserts into the database.