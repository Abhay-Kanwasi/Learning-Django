from django.urls import path
from . import views

url_pattern = [
    path("learn_django/",views.learn_django)    
]