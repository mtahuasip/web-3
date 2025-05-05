from django.urls import path
from . import views

urlpatterns = [
    path("listado-de-usuarios/", views.listado_usuarios, name="listado-de-usuarios")
]
