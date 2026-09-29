from django.db import models 

class Esporte(models.Model):
    nome = models.CharField(max_length=100)
    tecnico = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    email_tecnico = models.EmailField()
    imagem1 = models.ImageField(upload_to="fotos/")
    imagem2 = models.ImageField(upload_to="fotos/")
    imagem3 = models.ImageField(upload_to="fotos/")
    def __str__(self):
        return f"Esporte - {self.nome}"