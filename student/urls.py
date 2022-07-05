from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home_Student, name='Home_Student'),
    path('', views.subscribeToList, name='subscribeToList'),
]