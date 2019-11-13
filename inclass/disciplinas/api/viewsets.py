from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from disciplinas.models import Disciplina
from .serializers import DisciplinaSerializer
from inclass.gurobi import GurobiCalc

class DisciplinaViewSet(ModelViewSet):

    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer



class ResultadoViewSet(ModelViewSet):

     serializer_class = DisciplinaSerializer

     def list(self, request,*args, **kwargs):
        return Response(GurobiCalc())