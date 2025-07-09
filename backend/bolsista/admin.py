from django.contrib import admin
from .models import Bolsista, HorarioBolsista


@admin.register(Bolsista)
class BolsistaAdmin(admin.ModelAdmin):
    list_display = ("nome", "matricula", "curso", "periodo")
    search_fields = ("nome", "matricula", "curso")


@admin.register(HorarioBolsista)
class HorarioBolsistaAdmin(admin.ModelAdmin):
    list_display = ("bolsista", "get_dia_semana", "horario_inicio", "horario_fim")
    list_filter = ("dia_semana", "bolsista__curso")
    search_fields = ("bolsista__nome", "bolsista__matricula")

    def get_dia_semana(self, obj):
        return dict(obj.DIAS_SEMANA).get(obj.dia_semana, "Desconhecido")

    get_dia_semana.short_description = "Dia da Semana"
