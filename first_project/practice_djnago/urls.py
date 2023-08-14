from django.urls import path

from . import views


urlpatterns = [
    path('practice_django/', views.practice_django)
]