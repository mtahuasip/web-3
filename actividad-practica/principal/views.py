from django.shortcuts import render
from django.http import HttpResponse


def nombre(request):
    mensaje = "Matt Logan Tahuasi Pariamo"

    return HttpResponse(f"<h1>{mensaje}</h1>")


def inicio(request):
    mensaje = "Matt Logan Tahuasi Pariamo"

    return render(request, "inicio.html", {"mensaje": mensaje})
