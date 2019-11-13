from rest_framework.serializers import ModelSerializer
from horarios.models import Horario

class HorarioSerializer(ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'