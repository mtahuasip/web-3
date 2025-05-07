from django.shortcuts import render, get_list_or_404
from .models import Agenda


def listado_agendas(request):
    agendas = get_list_or_404(Agenda.objects.all())

    return render(request, "agenda/listado_agendas.html", {"agendas": agendas})
