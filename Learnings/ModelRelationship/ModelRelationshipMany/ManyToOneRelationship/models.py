from django.db import models

class User(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.user

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=30)
    post_details = models.CharField(max_length=40)
    publish_date = models.DateTimeField(auto_now_add=True)