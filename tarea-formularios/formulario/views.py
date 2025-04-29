from django.shortcuts import render
from .forms import FormularioUsuario


def formulario_usuario(request):
    if request.method == "POST":
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]

            ciudad_valor = form.cleaned_data["ciudad"]
            aficiones_valor = form.cleaned_data["aficiones"]
            sexo_valor = form.cleaned_data["sexo"]

            ciudad = dict(FormularioUsuario.CIUDADES_OPCIONES).get(ciudad_valor)
            aficiones = ", ".join(
                dict(FormularioUsuario.AFICIONES_OPCIONES).get(codigo)
                for codigo in aficiones_valor
            )
            sexo = dict(FormularioUsuario.SEXO_OPCIONES).get(sexo_valor)

            datos = {
                "nombre": nombre,
                "email": email,
                "ciudad": ciudad,
                "aficiones": aficiones,
                "sexo": sexo,
            }

            return render(request, "formulario/resumen_usuario.html", datos)
    else:
        form = FormularioUsuario()

    return render(request, "formulario/formulario_usuario.html", {"form": form})
