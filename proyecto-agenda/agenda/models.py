from django.db import models


class Agenda(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
