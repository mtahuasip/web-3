from django.urls import path
from . import views

urlpatterns = [
    path("listado-agendas/", views.listado_agendas, name="listado_agendas"),
    path("datos-personales/", views.datos_personales, name="datos_personales"),
]
