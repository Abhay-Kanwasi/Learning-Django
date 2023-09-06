from django.urls import path

from . import views

urlpatterns = [
    path('django_fees/', views.django_fees)
]
