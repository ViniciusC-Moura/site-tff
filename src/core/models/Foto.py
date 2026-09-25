from django.db import models
from .Esporte import Esporte

class Foto(models.Model):
    imagem = models.ImageField(upload_to="fotos/")
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE, related_name="foto", blank=True, null=True)
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
    competicao = models.CharField(max_length=100, choices=COMPETICAO_CHOICES, blank=True, null=True)
    edicao = models.CharField(max_length=100, blank=True, null=True)
    fase_competicao = models.CharField(choices=FASE_COMPETICAO_CHOICES, blank=True, null=True)
    evento = models.ForeignKey("Evento", on_delete=models.CASCADE, related_name="fotos", blank=True, null=True)

    def __str__(self):
        return f"Foto {self.esporte}"