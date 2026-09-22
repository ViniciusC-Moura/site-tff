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
        ('jerns', 'JERNS'),
    ]

    FASE_COMPETICAO_CHOICES = [
        ('polos', 'Polos'),
        ('estadual', 'Estadual'),
        ('nordeste', 'Nordeste'),
        ('nacional', 'Nacional')
    ]

    FASE_JOGOS_CHOICES = [
        ('Fase_de_grupos', 'Fase de Grupos'),
        ('64_avos', '64 avos'),
        ('32_avos', '32 avos'),
        ('16_avos', '16 avos'),
        ('oitavas', 'Oitavas'),
        ('quartas', 'Quartas'),
        ('semi', 'Semi'),
        ('final', 'Final'),
        
    ]

    placar_cnat = models.IntegerField()
    placar_adversario = models.IntegerField()
    nome_adversario = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=100)
    competicao = models.CharField(max_length=100, choices=COMPETICAO_CHOICES, blank=True)
    fase_competicao = models.CharField(choices=FASE_COMPETICAO_CHOICES)
    fase_jogo = models.CharField(choices=FASE_JOGOS_CHOICES)
    edicao = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='marcado')
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=100)

    def __str__(self):
        return f"CNAT {self.placar_cnat} x {self.placar_adversario} {self.nome_adversario}"