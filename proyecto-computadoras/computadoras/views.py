from django.shortcuts import render, get_list_or_404
from .models import Computadora


def listado_computadoras(request):
    computadoras = get_list_or_404(Computadora.objects.all())

    return render(
        request,
        "computadoras/listado_computadoras.html",
        {"computadoras": computadoras},
    )


def datos_personales(request):
    nombres = "Matt Logan"
    apellidos = "Tahuasi Pariamo"
    ci = "8406598"
    telefono = "67077485"
    correo = "mltahuasi@umsa.bo"

    return render(
        request,
        "computadoras/datos_personales.html",
        {
            "nombres": nombres,
            "apellidos": apellidos,
            "ci": ci,
            "telefono": telefono,
            "correo": correo,
        },
    )
