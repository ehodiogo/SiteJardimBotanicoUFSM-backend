from django.contrib import admin
from .models import Trilha, GuiaTrilha, Ponto


@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    list_display = ("nome", "get_dificuldade", "duracao", "get_qtd_pontos", "get_tags")
    search_fields = ("nome",)

    def get_dificuldade(self, obj):
        return dict(Trilha.DIFICULDADES).get(obj.dificuldade, "Desconhecida")

    get_dificuldade.short_description = "Dificuldade"

    def get_qtd_pontos(self, obj):
        return obj.pontos.count()

    get_qtd_pontos.short_description = "Total de Pontos"

    def get_tags(self, obj):
        return ", ".join(tag.tag for tag in obj.tags.all())

    get_tags.short_description = "Tags"


@admin.register(GuiaTrilha)
class GuiaTrilhaAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)


@admin.register(Ponto)
class PontoAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "descricao", "guia", "get_trilhas")
    search_fields = ("descricao",)
    list_filter = ("guia",)

    def get_trilhas(self, obj):
        return ", ".join(t.nome for t in Trilha.objects.filter(pontos=obj))

    get_trilhas.short_description = "Trilhas associadas"
