from django.urls import path
from . import views

urlpatterns = [
    path(
        "listado-de-publicaciones/",
        views.listado_publicaciones,
        name="listado-de-publicaciones",
    )
]
