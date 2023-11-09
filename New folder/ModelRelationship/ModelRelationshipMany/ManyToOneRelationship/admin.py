from django.contrib import admin
from .models import User, Post

class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'password']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post_name', 'post_details']

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)