from django.shortcuts import render
from .forms import FormularioPrincipal


def nuevo_usuario(request):
    if request.method == "POST":
        form = FormularioPrincipal(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            fecha_nacimiento = form.cleaned_data["fecha_nacimiento"]
            genero = form.cleaned_data["genero"]
            clave = form.cleaned_data["clave"]

            datos = {
                "nombre": nombre,
                "apellido": apellido,
                "fecha_nacimiento": fecha_nacimiento,
                "genero": genero,
                "clave": clave,
            }

            return render(request, "principal/nuevo_usuario.html", datos)
    else:
        form = FormularioPrincipal()

    return render(request, "principal/registra_usuario.html", {"form": form})
