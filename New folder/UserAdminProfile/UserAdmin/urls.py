from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.user_profile, name="dashboard"),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('userdetails/<int:id>/', views.user_details, name="userdetails")
]
