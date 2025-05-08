from django.db import models


class Computadora(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    cap_hd = models.IntegerField()
    cap_ram = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.modelo} {self.marca}"
