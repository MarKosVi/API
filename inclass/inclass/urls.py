from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from disciplinas.api.viewsets import DisciplinaViewSet
from disciplinas.api.viewsets import ResultadoViewSet
from escolas.api.viewsets import EscolaViewSet
from horarios.api.viewsets import HorarioViewSet
from salas.api.viewsets import SalaViewSet
from turmas.api.viewsets import TurmaViewSet

router = routers.DefaultRouter()
router.register(r'disciplina', DisciplinaViewSet, base_name='Disciplina')
router.register(r'resultado', ResultadoViewSet, base_name='Disciplina')
router.register(r'escola', EscolaViewSet, base_name='Escola')
router.register(r'horario', HorarioViewSet, base_name='Horario')
router.register(r'sala', SalaViewSet, base_name='Sala')
router.register(r'turma', TurmaViewSet, base_name='Turma')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
