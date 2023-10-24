from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('set/', views.setcookie, name="set"),
    path('get/', views.getcookie, name="get"),
    path('del/', views.delcookie, name="del"),
    path('signedset/', views.signed_set_cookie, name="signedset"),
    path('signedget/', views.signed_get_cookie, name="signedget"),
]
