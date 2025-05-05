from django.shortcuts import render, get_list_or_404
from .models import Publicacion


def listado_publicaciones(request):
    publicaciones = get_list_or_404(Publicacion.objects.all())

    return render(
        request,
        "publicaciones/listado_publicaciones.html",
        {"publicaciones": publicaciones},
    )
