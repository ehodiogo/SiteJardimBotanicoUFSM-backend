from rest_framework import serializers
from .models import ConfiguracaoJB


class ConfiguracaoJBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracaoJB
        fields = "__all__"
