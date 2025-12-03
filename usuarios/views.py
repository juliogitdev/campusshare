from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1> Bem vindo a rota de usuarios</h1>")