from django.db import models

class Jogo(models.Model):
    STATUS_CHOICES = [
        ('marcado', 'Marcado'),
        ('finalizado', 'Finalizado'),
    ]

    COMPETICAO_CHOICES = [
        ('jerns', 'JERNS'),
        ('jebs', 'JEBS'),
        ('juverns', 'JUVERNS'),
        ('fnde', 'FNDE'),
        ('intercampi', 'Intercampi'),
        ('jifs', 'JIFs'),
        ('', 'JERNS'),
    ]

    placar_cnat = models.IntegerField()
    placar_adversario = models.IntegerField()
    nome_adversario = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=100)
    competicao = models.CharField(max_length=100, choices=COMPETICAO_CHOICES, blank=True)
    fase_competicao = models.CharField(max_length=100)
    fase_jogo = models.CharField(max_length=100)
    edicao = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='marcado')
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=100)

    def __str__(self):
        return f"CNAT {self.placar_cnat} x {self.placar_adversario} {self.nome_adversario}"