from django.urls import path
from . import views

urlpatterns = [
    path("saludo/<str:nombre>", views.saludo_usuario),
    path("verifica-comentarios/<int:numero>", views.verifica_numero),
    path("vista-parametrizada/<str:cadena>/<int:dato_num>", views.recibe_params),
]
