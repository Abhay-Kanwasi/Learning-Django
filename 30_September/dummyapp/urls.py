import profile

from django.urls import path
from .views import home, about, user_profile

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('profile/', user_profile, name='profile'),
]