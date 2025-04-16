from django.urls import path
from . import views

urlpatterns = [
    path("saludo-principal/", views.vista_saludo, name="saludo-principal"),
    path("saludo-avanzado/", views.SaludoAvanzado.as_view(), name="saludo-avanzado"),
    path(
        "vista-con-parametros/<str:nombre>/<int:edad>/<int:anio>/",
        views.VistaParametrizada.as_view(),
        name="vista-param",
    ),
]
