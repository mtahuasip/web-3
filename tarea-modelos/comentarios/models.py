from django.db import models
from django.contrib.auth.models import User
from publicaciones.models import Publicacion


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comentario de {self.autor.username} en "{self.publicacion}": {self.contenido[:30]}...'
