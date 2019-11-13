from rest_framework.serializers import ModelSerializer
from escolas.models import Escola

class EscolaSerializer(ModelSerializer):
    class Meta:
        model = Escola
        fields = '__all__'