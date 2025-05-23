from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse
from .models import Publicacion, Comentario
from .forms import PublicacionForm, ComentarioForm
from django.contrib.auth import logout


# Create your views here.
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()  # select * from publicacion
    return render(
        request, "blog/lista_publicaciones.html", {"publicaciones": publicaciones}
    )


def crear_publicacion(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden(
            "Necesita tener una sesión para poder crear una publicación"
        )

    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.usuario = request.user
            publicacion.save()
            return redirect("lista_publicaciones")
    else:
        form = PublicacionForm()
    return render(request, "blog/crear_publicacion.html", {"form": form})


def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentarios = Comentario.objects.filter(publicacion=publicacion)
    form_comentario = ComentarioForm() if request.user.is_authenticated else None
    contexto = {
        "publicacion": publicacion,
        "comentarios": comentarios,
        "form_comentario": form_comentario,
    }
    return render(request, "blog/detalle_publicacion.html", contexto)


def agregar_comentario(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.publicacion = publicacion
            comentario.save()
            return redirect("detalle_publicacion", pk=pk)


def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)

    if publicacion.usuario != request.user:
        return HttpResponseForbidden("no tiene permiso para editar esta publicación")

    if request.method == "POST":
        form = PublicacionForm(request.POST, instance=publicacion)

        if form.is_valid():
            form.save()
            return redirect("detalle_publicacion", pk=publicacion.pk)
    else:
        form = PublicacionForm(instance=publicacion)

    return render(request, "blog/editar_publicacion.html", {"form": form})


def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)

    if publicacion.usuario != request.user:
        return HttpResponseForbidden("No puedes eliminar esta publicación")

    if request.method == "POST":
        publicacion.delete()
        return redirect("lista_publicaciones")

    return render(
        request,
        "blog/confirmar_eliminacion.html",
        {"publicacion": publicacion},
    )


def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.user != comentario.usuario:
        return HttpResponseForbidden("No puedes editar este comentario")

    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect("detalle_publicacion", pk=comentario.publicacion.pk)
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, "blog/editar_comentario.html", {"form": form})


def principal(request):
    return redirect("lista_publicaciones")


def logout_view(request):
    logout(request)
    return redirect("lista_publicaciones")


def lista_integrantes(request):
    lista = [
        "Aquise Guarachi Massiel Damaris C. I. 12768063",
        "Arismendi Quispe Ysrael C. I. 6981807",
        "Tahuasi Pariamo Matt Logan C. I. 8406598",
    ]

    respuesta = ""
    for inte in lista:
        respuesta = respuesta + f"<p>{inte}</p>"

    return HttpResponse(respuesta)
