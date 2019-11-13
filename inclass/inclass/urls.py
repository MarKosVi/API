from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from disciplinas.api.viewsets import DisciplinaViewSet
from escolas.api.viewsets import EscolaViewSet
from horarios.api.viewsets import HorarioViewSet
from salas.api.viewsets import SalaViewSet
from turmas.api.viewsets import TurmaViewSet

router = routers.DefaultRouter()
router.register(r'disciplina', DisciplinaViewSet)
router.register(r'escola', EscolaViewSet)
router.register(r'horario', HorarioViewSet)
router.register(r'sala', SalaViewSet)
router.register(r'turma', TurmaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
