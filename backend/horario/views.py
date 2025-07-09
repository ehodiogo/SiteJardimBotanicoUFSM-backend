from rest_framework import viewsets
from .models import ConfiguracaoJB
from .serializers import ConfiguracaoJBSerializer


class ConfiguracaoJBViewSet(viewsets.ModelViewSet):
    queryset = ConfiguracaoJB.objects.all()
    serializer_class = ConfiguracaoJBSerializer
