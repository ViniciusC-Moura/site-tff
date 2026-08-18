from django.db import models 

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    parcelas = models.IntegerField()

    def __str__(self):
        return self.nome