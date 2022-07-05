from django.shortcuts import render
from django.http import HttpResponse

def Home_Student(request):
    return HttpResponse("Ola estudante")

def subscribeToList(request):
    return HttpResponse("Lista Assinada")