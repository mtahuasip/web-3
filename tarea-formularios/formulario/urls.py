from django.urls import path
from . import views

urlpatterns = [
    path(
        "formulario-usuario/",
        views.formulario_usuario,
        name="formulario_usuario",
    )
]
