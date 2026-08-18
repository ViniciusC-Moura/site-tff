from django.db import models
class Foto(models.Model):
    imagem = models.ImageField(upload_to="fotos/")
    def __str__(self):
        return f"Foto {self.id}"