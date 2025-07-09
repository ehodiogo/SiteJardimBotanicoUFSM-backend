from rest_framework import serializers
from .models import QuizAmostra
from amostras.serializers import AmostraSerializer
class QuizAmostraSerializer(serializers.ModelSerializer):
    amostra = AmostraSerializer(read_only=True)
    class Meta:
        model = QuizAmostra
        fields = "__all__"
