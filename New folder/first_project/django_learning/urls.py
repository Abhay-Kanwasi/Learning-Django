from django.urls import path

from . import views


urlpatterns = [
    path("learn_django/", views.learn_djnago),
    path("learn_python/", views.learn_python),
    path("learn_github/", views.learn_github),
]
