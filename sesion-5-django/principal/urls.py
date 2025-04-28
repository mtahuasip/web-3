from django.urls import path
from . import views

urlpatterns = [path("nuevo-usuario/", views.nuevo_usuario, name="nuevo-usuario")]
