from django.urls import path
from . import views

urlpatterns = [
    path("nombre/", views.nombre, name="nombre"),
    path("inicio/", views.inicio, name="inicio"),
]
