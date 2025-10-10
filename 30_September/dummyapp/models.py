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