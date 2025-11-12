import profile

from django.urls import path
from .views import home, about, user_profile, create_article

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('profile/', user_profile, name='profile'),
    path('article/new/', create_article, name='create_article'),
]