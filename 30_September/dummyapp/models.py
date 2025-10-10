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


from django.db import models

# Independent Models
class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Form(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Pricing(models.Model):
    price = models.DecimalField(max_digits=4, decimal_places=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.price)

class Workflow(models.Model):
    name = models.CharField(max_length=14)
    details = models.CharField(max_length=30)

    def __str__(self):
        return self.details

# Relationship Models
class Tasks(models.Model):
    name = models.CharField(max_length=24)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='tasks')
    task_details = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    pricing = models.OneToOneField(Pricing, on_delete=models.CASCADE, default=0.0)
    categories = models.ManyToManyField(Category, related_name="services")
    form = models.ManyToManyField(Form, related_name="services")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name