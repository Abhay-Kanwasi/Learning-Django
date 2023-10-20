from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name="profile"),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('changepassword/', views.user_changepassword, name='changepassword'),
    path('changepassword1/', views.user_changepassword1, name='changepassword1'),
    path('showuserprofile/', views.show_userprofile, name="showprofile"),
]