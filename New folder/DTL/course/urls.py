from django.urls import path
from . import views

urlpatterns = [
    path("learn_django/",views.learn_django)    
]