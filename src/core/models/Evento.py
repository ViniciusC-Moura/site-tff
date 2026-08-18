from django.db import models
from .Tag import Tag
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(
        upload_to="eventos/",
        blank=True,
        null=True
    )
    local = models.CharField(max_length=200)
    data_hora = models.DateTimeField()
    tag = models.OneToOneField(
        Tag,
        on_delete=models.CASCADE,
        related_name="evento"
    )
    def __str__(self):
        return self.titulo