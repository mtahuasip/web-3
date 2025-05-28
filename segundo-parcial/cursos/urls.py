from django.urls import path
from . import views

urlpatterns = [
    path("listado_cursos/", views.listado_cursos, name="listado_cursos"),
    path("detalle_curso/<int:codigo>/", views.detalle_curso, name="detalle_curso"),
]
