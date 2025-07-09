from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmostraViewSet, DadosCientificosViewSet
from trilhas.views import TrilhaViewSet
from presenca.views import PresencaViewSet
from bolsista.views import BolsistaViewSet, HorarioBolsistaViewSet
from agendamento.views import AgendamentoViewSet, AgendamentosHoje
from horario.views import ConfiguracaoJBViewSet
from quiz.views import QuizAmostraViewSet

router = DefaultRouter()
router.register(r'amostras', AmostraViewSet)
router.register(r'dados-cientificos', DadosCientificosViewSet)
router.register(r"trilhas", TrilhaViewSet)
router.register(r"presenca", PresencaViewSet)
router.register(r"bolsistas", BolsistaViewSet)
router.register(r"horarios-bolsistas", HorarioBolsistaViewSet)
router.register(r"agendamentos", AgendamentoViewSet)
router.register(r"agendamentos-hoje", AgendamentosHoje, basename="agendamentos-hoje")
router.register(r"configuracoes", ConfiguracaoJBViewSet)
router.register(r"quiz", QuizAmostraViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
