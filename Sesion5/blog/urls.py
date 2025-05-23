from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("lista_publicaciones/", views.lista_publicaciones, name="lista_publicaciones"),
    path("crear_publicacion/", views.crear_publicacion, name="crear_publicacion"),
    path("publicacion/<int:pk>", views.detalle_publicacion, name="detalle_publicacion"),
    path(
        "publicacion/<int:pk>/comentar/",
        views.agregar_comentario,
        name="agregar_comentario",
    ),
    path(
        "publicacion/<int:pk>/editar/",
        views.editar_publicacion,
        name="editar_publicacion",
    ),
    path(
        "publicacion/<int:pk>/eliminar/",
        views.eliminar_publicacion,
        name="eliminar_publicacion",
    ),
    path(
        "", RedirectView.as_view(url="/lista_publicaciones/", permanent=False)
    ),  # Redirige "/" a "/lista_publicaciones"
    path(
        "comentario/<int:pk>/editar/", views.editar_comentario, name="editar_comentario"
    ),
    path("principal/", views.principal, name="principal"),
    path("logout/", views.logout_view, name="logout"),
    path("lista_integrantes/", views.lista_integrantes, name="lista_integrantes"),
]
