from django.db import models
from .Esporte import Esporte

class Figurinha(models.Model):
    imagem = models.ImageField(upload_to="figurinhas/")
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE, related_name="figurinhas")

    def __str__(self):
        return f"Figurinha {self.id}"