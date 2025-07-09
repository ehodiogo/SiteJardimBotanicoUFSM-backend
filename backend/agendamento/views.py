from rest_framework import viewsets
from .models import Agendamento
from .serializers import AgendamentoSerializer
import datetime

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class AgendamentosHoje(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    def get_queryset(self):
        return self.queryset.filter(data_agendamento= datetime.date.today())