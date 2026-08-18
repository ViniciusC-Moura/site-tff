from django.db import models

class Gestor(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='gestores/')

    def __str__(self):
        return self.nome