from rest_framework.viewsets import ModelViewSet
from escolas.models import Escola
from .serializers import EscolaSerializer

class EscolaViewSet(ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer