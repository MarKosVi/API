from rest_framework.serializers import ModelSerializer
from turmas.models import Turma

class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'