from django.db import models
from .fotos import Foto
class Tag(models.Model):
    nome = models.CharField(max_length=100)
    fotos = models.ManyToManyField(
        Foto,
        related_name="tags",
        blank=True
    )
    def __str__(self):
        return self.nome
