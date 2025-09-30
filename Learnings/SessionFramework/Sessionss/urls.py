from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('set/', views.setsession, name="set"),
    path('get/', views.getsession, name="get"),
    path('del/', views.delsession, name="del"),
    path('settestcookie/', views.settestcookie, name="settestcookie"),
    path('checktestcookie/', views.checktestcookie, name="checktestcookie"),
    path('deltestcookie/', views.deltestcookie, name="deltestcookie"),
]
