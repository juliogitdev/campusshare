from django.shortcuts import render
from django.http import HttpResponse

def pagina_inicial(request):
    return HttpResponse("<h1> Bem-vindo à Rede Social Universitária!</h1>")
# Create your views here.
