from django.db import models
from django.contrib.auth.models import User


class Publicacion(models.Model):
    titulo = models.CharField(max_length=20)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
