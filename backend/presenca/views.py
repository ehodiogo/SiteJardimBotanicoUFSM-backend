from rest_framework import viewsets
from .models import Presenca
from .serializers import PresencaSerializer


class PresencaViewSet(viewsets.ModelViewSet):
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer
