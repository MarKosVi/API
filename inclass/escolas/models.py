from django.db import models

class Escola(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60, null=False, blank = False)

    def __str__(self):
        return self.nome
