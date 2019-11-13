from django.db import models
from escolas.models import Escola

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45, null=False, blank = False)
    tipo_sala = models.IntegerField()
    id_escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
