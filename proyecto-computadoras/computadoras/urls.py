from django.urls import path
from . import views

urlpatterns = [
    path(
        "listado-computadoras/", views.listado_computadoras, name="listado_computadoras"
    ),
    path("datos-personales/", views.datos_personales, name="datos_personales"),
]
