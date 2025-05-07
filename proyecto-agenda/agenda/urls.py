from django.urls import path
from . import views

urlpatterns = [path("listado-agendas/", views.listado_agendas)]
