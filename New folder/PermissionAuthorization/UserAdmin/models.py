from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)