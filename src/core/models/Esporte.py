from django.db import models 

class Esporte(models.Model):
    nome = models.CharField(max_length=100)
    tecnico = models.CharField(max_length=255)

    def __str__(self):
        return f"Esporte - {self.nome}"