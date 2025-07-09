from rest_framework import viewsets
from .models import Bolsista, HorarioBolsista
from .serializers import BolsistaSerializer, HorarioBolsistaSerializer


class BolsistaViewSet(viewsets.ModelViewSet):
    queryset = Bolsista.objects.all()
    serializer_class = BolsistaSerializer


class HorarioBolsistaViewSet(viewsets.ModelViewSet):
    queryset = HorarioBolsista.objects.all()
    serializer_class = HorarioBolsistaSerializer
