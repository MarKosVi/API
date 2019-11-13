from django.db import models
from escolas.models import Escola

class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    qtd_alunos = models.IntegerField()
    cod_turma = models.CharField(max_length=45, null=False, blank = False)
    curso = models.CharField(max_length=45, null=False, blank = False)
    turno = models.CharField(max_length=45, null=False, blank = False)
    id_escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    def __str__(self):
        return self.cod_turma