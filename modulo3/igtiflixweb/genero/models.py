from django.db import models

# Create your models here.
class Genero(models.Model):
    descricao = models.CharField(max_length=50) # tamanho máximo do campo

    def __str__(self):
        return self.descricao