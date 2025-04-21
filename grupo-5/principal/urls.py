from django.urls import path
from . import views

urlpatterns = [
    path("lista-grupo/", views.nomina_grupo, name="lista-grupo"),
    path("tabla/<int:numero>/", views.tabla, name="tabla"),
    path(
        "calculadora/<str:operacion>/<int:numero1>/<int:numero2>/",
        views.operacion,
        name="calculadora",
    ),
]
