from django.db import models
from django.contrib.auth.models import AbstractUser

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


"""
Model Relationships

Django offers way to define the 3 most common types of database relationships.
"""

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

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    # boolean fields
    is_verified = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_display_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.username}"

    def has_premium_access(self):
        return True if self.is_premium else False


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title