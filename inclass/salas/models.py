from django.db import models
from escolas.models import Escola

class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    campus = models.ForeignKey(Escola, on_delete=models.CASCADE)
    tipo_sala = models.IntegerField()

    def __str__(self):
        return self.tipo_sala