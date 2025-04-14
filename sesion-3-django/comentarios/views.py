from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def saludo_usuario(request, nombre):
    date = datetime.now()
    year = date.year

    return HttpResponse(
        f"<h1>Hola <strong>{nombre.capitalize()}</strong>, te saluda Django 😎 en el año {year}</h1>"
    )


def verifica_numero(request, numero):
    if numero % 2 == 0:
        message = "par ✌️"
    else:
        message = "impar 🤞"

    return HttpResponse(f"<h1>El numero {numero} es {message}</h1>")


def recibe_params(request, cadena, dato_num):
    return HttpResponse(f"<h1>Se escribió {cadena} y el numero {dato_num} 😊</h1>")
