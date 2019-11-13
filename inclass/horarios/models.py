from django.db import models

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    horario = models.CharField(max_length=45, null=False, blank = False)
    dia_semana = models.CharField(max_length=45, null=False, blank = False)

    def __str__(self):
        return self.horario