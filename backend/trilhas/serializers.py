
from rest_framework import serializers
from .models import Trilha, Ponto, GuiaTrilha


class GuiaTrilhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaTrilha
        fields = ["descricao", "proximo_passo"]


class PontoSerializer(serializers.ModelSerializer):
    guia = GuiaTrilhaSerializer()

    class Meta:
        model = Ponto
        fields = ["id", "latitude", "longitude", "descricao", "order", "guia", "imagem"]


class TrilhaSerializer(serializers.ModelSerializer):
    pontos = PontoSerializer(many=True)
    tags = serializers.SerializerMethodField()

    def get_tags(self, obj):
        return [tag.tag for tag in obj.tags.all()]

    class Meta:
        model = Trilha
        fields = ["id", "nome", "pontos", "duracao", "dificuldade", "tags"]
