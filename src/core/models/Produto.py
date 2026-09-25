from django.db import models 

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    parcelas = models.IntegerField()
    link = models.URLField()
    imagem = models.ImageField(upload_to='produtos/')

    @property
    def valor_parcela(self):
        if self.parcelas > 0:
            return self.preco / self.parcelas
        return self.preco
        
    def __str__(self):
        return self.nome