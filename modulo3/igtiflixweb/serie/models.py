from django.db import models

# Create your models here.

# ligação com o banco de dados e população do form
class Serie(models.Model):
    idGenero = models.ForeignKey("genero.Genero", on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome