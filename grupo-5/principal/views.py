from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def nomina_grupo(request):
    integrantes = [
        "Chavarria De La Cruz Leonor Belen CI. 9885133",
        "Alvarado Ticona Pedro Fernando CI. 14006696",
        "Calle Nina Pedro Enrrique CI. 9201235",
        "Gutierrez Quipe Victor Andres CI. 7028027",
        "Aquise Guarachi Massiel Damaris CI. 12768063",
        "Portillo Herrera Marcelo CI. 6129896",
        "Tahuasi Pariamo Matt  CI. 8406598",
    ]
    respuesta = f"<ol style='list-style: lower-alpha'>"
    for integrante in integrantes:
        respuesta += f"<li>{integrante}</li>"

    respuesta += "</ol>"
    return HttpResponse(f"<h1>NOMINA DE GRUPO</h1>{respuesta}")


def tabla(request, numero):
    tabla_numero = ""
    for i in range(1, 11):
        tabla_numero += f"<p>{numero} x {i} = {numero*i}</p>"

    return HttpResponse(
        f"<h1>Tabla de Multiplicar del numero {numero}</h1>{tabla_numero}"
    )


def operacion(requets, operacion, numero1, numero2):
    resultado = ""
    if operacion == "sumar":
        resultado = f"{numero1} + {numero2} = {numero2+numero2}"
    elif operacion == "restar":
        resultado = f"{numero1} - {numero2} = {numero2-numero2}"
    elif operacion == "multiplicar":
        resultado = f"{numero1} x {numero2} = {numero2*numero2}"
    elif operacion == "dividir":
        if numero2 > 0:
            resultado = f"{numero1} / {numero2} = {numero1/numero2}"
        else:
            resultado = "El numero 2 debe ser mayor a cero"
    else:
        resultado = "La operación debe ser SUMAR, RESTAR, DIVIDIR O MULTIPLICAR"

    return HttpResponse(resultado)
