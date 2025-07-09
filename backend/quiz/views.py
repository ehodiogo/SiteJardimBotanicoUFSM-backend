from rest_framework import viewsets
from .models import QuizAmostra
from .serializers import QuizAmostraSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class QuizAmostraViewSet(viewsets.ModelViewSet):
    queryset = QuizAmostra.objects.all()
    serializer_class = QuizAmostraSerializer

    @action(detail=False, url_path="amostra/(?P<amostra_id>[^/.]+)")
    def by_amostra(self, request, amostra_id=None):
        queryset = self.get_queryset().filter(amostra__id=amostra_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
