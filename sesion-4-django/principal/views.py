from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


# Vista basado en Función
def vista_saludo(request):
    return HttpResponse("<h1>Hola desde Django</h1>")


# Vista basada en Clases


class SaludoAvanzado(TemplateView):
    template_name = "inicio.html"


class VistaParametrizada(TemplateView):
    template_name = "lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Recuperar los parámetros
        nombre = self.kwargs.get("nombre")
        edad = self.kwargs.get("edad")
        anio = self.kwargs.get("anio")

        # Procesar los datos
        nombre_mayusculas = nombre.upper()

        # Preparar nuevo contexto para ser desplegado en el template
        context["nombre"] = nombre_mayusculas
        context["edad"] = edad
        context["anio"] = anio

        return context
