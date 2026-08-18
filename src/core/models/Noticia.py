from django.db import models
from .Tag import Tag
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(
        upload_to="noticias/",
        blank=True,
        null=True
    )
    data = models.DateTimeField()
    descricao = models.CharField(max_length=500)
    conteudo = models.TextField()
    tags = models.ManyToManyField(
        Tag,
        related_name="noticias",
        blank=True
    )
    def __str__(self):
        return self.titulo