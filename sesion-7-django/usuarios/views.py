from django.shortcuts import render, get_list_or_404
from django.contrib.auth.models import User


def listado_usuarios(request):
    usuarios = get_list_or_404(User.objects.all())

    return render(request, "usuarios/listado_usuarios.html", {"usuarios": usuarios})
