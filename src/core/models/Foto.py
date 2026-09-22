from django.db import models
from .Esporte import Esporte

class Foto(models.Model):
    imagem = models.ImageField(upload_to="fotos/")
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE, related_name="foto")
    COMPETICAO_CHOICES = [
            ('jerns', 'JERNS'),
            ('jebs', 'JEBS'),
            ('juverns', 'JUVERNS'),
            ('fnde', 'FNDE'),
            ('intercampi', 'Intercampi'),
            ('jifs', 'JIFs'),
            ('jerns', 'JERNS'),
        ]

    FASE_COMPETICAO_CHOICES = [
        ('polos', 'Polos'),
        ('estadual', 'Estadual'),
        ('nordeste', 'Nordeste'),
        ('nacional', 'Nacional')
    ]
    competicao = models.CharField(max_length=100, choices=COMPETICAO_CHOICES, blank=True)
    edicao = models.CharField(max_length=100)
    fase_competicao = models.CharField(choices=FASE_COMPETICAO_CHOICES)

    def __str__(self):
        return f"Foto {self.esporte}"