from django.urls import path, include
from . import views
 
urlpatterns = [
    path('teacher/add', views.criarProfessor, name="addTeacher"),
 ]