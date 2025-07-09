from rest_framework import viewsets
from .models import Amostra, DadosCientificos
from .serializers import AmostraSerializer, DadosCientificosSerializer

class DadosCientificosViewSet(viewsets.ModelViewSet):
    queryset = DadosCientificos.objects.all()
    serializer_class = DadosCientificosSerializer

class AmostraViewSet(viewsets.ModelViewSet):
    queryset = Amostra.objects.all()
    serializer_class = AmostraSerializer
