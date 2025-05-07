from django.shortcuts import render, get_list_or_404
from .models import Agenda


def listado_agendas(request):
    agendas = get_list_or_404(Agenda.objects.all())

    return render(request, "agenda/listado_agendas.html", {"agendas": agendas})


def datos_personales(request):
    nombres = "Matt Logan"
    apellidos = "Tahuasi Pariamo"
    ci = "8406598"
    telefono = "67077485"
    correo = "mltahuasi@umsa.bo"

    return render(
        request,
        "agenda/datos_personales.html",
        {
            "nombres": nombres,
            "apellidos": apellidos,
            "ci": ci,
            "telefono": telefono,
            "correo": correo,
        },
    )
