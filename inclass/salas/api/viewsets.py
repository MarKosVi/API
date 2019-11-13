from rest_framework.viewsets import ModelViewSet
from salas.models import Sala
from .serializers import SalaSerializer

class SalaViewSet(ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer