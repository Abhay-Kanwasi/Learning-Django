from django.urls import path
from enroll import views

urlpatterns = [
    path('show/',views.show_details)
]
