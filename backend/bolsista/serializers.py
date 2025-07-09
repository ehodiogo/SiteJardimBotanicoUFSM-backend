from rest_framework import serializers
from .models import Bolsista, HorarioBolsista


class BolsistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolsista
        fields = "__all__"


class HorarioBolsistaSerializer(serializers.ModelSerializer):
    bolsista = serializers.PrimaryKeyRelatedField(queryset=Bolsista.objects.all())

    class Meta:
        model = HorarioBolsista
        fields = "__all__"
