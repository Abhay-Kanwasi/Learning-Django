from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.CharField(max_length=25)
    quantity = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    is_available = models.CharField(max_length=25)