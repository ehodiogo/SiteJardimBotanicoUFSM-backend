from rest_framework import serializers
from .models import Amostra, DadosCientificos

class DadosCientificosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosCientificos
        fields = '__all__'

class AmostraSerializer(serializers.ModelSerializer):
    dados_cientificos = DadosCientificosSerializer(read_only=True)

    class Meta:
        model = Amostra
        fields = '__all__'
