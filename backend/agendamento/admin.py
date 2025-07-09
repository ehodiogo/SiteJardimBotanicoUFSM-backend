from django.contrib import admin
from .models import Agendamento


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = (
        "nome_escola_instituto",
        "data_agendamento",
        "horario_pretendido",
        "primeira_atividade",
        "segunda_atividade",
        "bolsistas_disponiveis",
    )

    readonly_fields = ("bolsistas_disponiveis",)

    fieldsets = (
        (
            "Informações da Instituição",
            {
                "fields": (
                    "nome_escola_instituto",
                    "tipo_institituicao",
                    "nivel_instituicao",
                    "municipio",
                    "endereco_escola_instituto",
                    "ano_serie_semestre_turma",
                    "numero_previsto_visitantes",
                    "nome_responsavel",
                    "telefone",
                    "email",
                )
            },
        ),
        (
            "Agendamento",
            {
                "fields": (
                    "data_agendamento",
                    "horario_pretendido",
                    "tempo_disponivel",
                    "bolsistas_disponiveis",
                )
            },
        ),
        (
            "Atividades",
            {
                "fields": (
                    "primeira_atividade",
                    "segunda_atividade",
                )
            },
        ),
        (
            "Conteúdo e Acessibilidade",
            {
                "fields": (
                    "aliar_conteudo_escolar",
                    "conteudo_escolar",
                    "necessaria_adaptacao",
                    "adaptacao_descricao",
                )
            },
        ),
        ("Outros", {"fields": ("piquenique",)}),
    )

    def bolsistas_disponiveis(self, obj):
        if not obj.data_agendamento or not obj.horario_pretendido:
            return "Preencha a data e o horário"
        bolsistas = obj.buscar_bolsista()
        if bolsistas.exists():
            return ", ".join([b.nome for b in bolsistas])
        return "Nenhum disponível"

    bolsistas_disponiveis.short_description = "Bolsistas disponíveis"
