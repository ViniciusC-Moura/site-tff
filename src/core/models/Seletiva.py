from django.db import models 
class Seletiva(models.Model):
    data = models.DateTimeField()
    local = models.CharField(max_length=255)
    hora = models.CharField(max_length=50)
    esporte = models.OneToOneField(Esporte, on_delete=models.CASCADE, related_name="seletiva")

    def __str__(self):
        return f"Seletiva em {self.local}"