from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Vista basado en función


def saludo(request):
    return HttpResponse("¡Hola, mundo!")


def saludo_personalizado(request):
    return HttpResponse("Hola, te saludo tu amigo Django")
