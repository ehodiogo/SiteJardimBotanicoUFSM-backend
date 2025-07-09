from django.db import models
from django.db.models import TextChoices
from bolsista.models import Bolsista, HorarioBolsista

class TiposInstituicao(TextChoices):
    publica_municipal = 'publica_municipal', 'Pública Municipal'
    publica_estadual = "publica_estadual", "Pública Estadual"
    publica_federal = "publica_federal", "Pública Federal"
    privada = 'privada', 'Privada'
    filantropica = 'filantropica', 'Filantropica'
    outro = 'outro', 'Outro'

class NiveisInstituicao(TextChoices):
    infantil = 'infantil', 'Educação Infantil'
    fundamental_inicial = 'fundamental_inicial', 'Educação Fundamental - Séries Iniciais'
    fundamental_finail = 'fundamental_final', 'Educação Fundamental - Séries Finais'
    medio = 'medio', 'Ensino Médio'
    superior = 'superior', 'Ensino Superior'
    nao_escolar = 'nao_escolar', 'Não escolar'

class AtividadesPrimarias(TextChoices):

    caminhada_guiada = 'caminhada_guiada', 'Caminhada guiada pelo Jardim Botânico (1h30-2h) - todas as idades'
    telhado_verde = 'telhado_verde', 'Telhado verde e agenda 2030 (até 40 min) - a partir de 9 anos'
    jardim_sensorial = 'jardim_sensorial', 'Jardim Sensorial (até 30 min) - todas as idades'
    exposicao_taxidermia = 'exposicao_taxidermia', 'Exposição de animais taxidermizados - todas as idades'
    palestra_peconhentos = 'palestra_peconhentos', 'Palestra sobre prevenção de acidentes com animais peçonhentos - a partir de 9 anos'
    chapeuzinho_verde = 'chapeuzinho_verde', '“Chapeuzinho Verde e o Jardim Encantado” (pré ao 2º ano)'
    horta_mandala = 'horta_mandala', 'Visita à horta mandala do Jardim Botânico - horta sustentável (terças de manhã)'
    artesanato_botanico = 'artesanato_botanico', 'Artesanato botânico (terças de manhã e quartas à tarde)'
    culinaria_pancs = 'culinaria_pancs', 'Culinária com PANCS (terças de manhã e quartas à tarde)'

class AtividadesSecundarias(TextChoices):
    caminhada_guiada = 'caminhada_guiada', 'Caminhada guiada pelo Jardim Botânico (1h30-2h) - a partir de 9 anos'
    telhado_verde = 'telhado_verde', 'Telhado verde e agenda 2030 (até 40 min) - a partir de 9 anos'
    jardim_sensorial = 'jardim_sensorial', 'Jardim Sensorial (até 30 min) - todas as idades'
    exposicao_taxidermia = 'exposicao_taxidermia', 'Exposição de animais taxidermizados - todas as idades'
    palestra_peconhentos = 'palestra_peconhentos', 'Palestra sobre prevenção de acidentes com animais peçonhentos - a partir de 9 anos'

class Agendamento(models.Model):

    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    nome_escola_instituto = models.CharField(max_length=255)
    nome_responsavel = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    endereco_escola_instituto = models.CharField(max_length=255, blank=True, null=True)
    tipo_institituicao  = models.CharField(max_length=20, choices=TiposInstituicao.choices, default=TiposInstituicao.outro)
    nivel_instituicao = models.CharField(max_length=55, choices=NiveisInstituicao.choices, default=NiveisInstituicao.nao_escolar)
    ano_serie_semestre_turma = models.CharField(max_length=255, blank=True, null=True)
    numero_previsto_visitantes = models.CharField(max_length=255, blank=True, null=True)

    data_agendamento = models.DateField()
    tempo_disponivel = models.TimeField()
    horario_pretendido = models.TimeField()

    # acessibilidade
    necessaria_adaptacao = models.BooleanField(default=False)
    adaptacao_descricao = models.TextField(blank=True, null=True)

    # atividades

    primeira_atividade = models.CharField(max_length=255, choices=AtividadesPrimarias.choices)
    segunda_atividade = models.CharField(max_length=255, choices=AtividadesSecundarias.choices)

    # conteudo

    aliar_conteudo_escolar = models.BooleanField(default=False)
    conteudo_escolar = models.TextField(blank=True, null=True)

    # piqueniques

    piquenique = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Agendamento do Jardim Botânico'
        verbose_name_plural = 'Agendamentos do Jardim Botânico'

    def buscar_bolsista(self):
        dia_semana = self.data_agendamento.weekday()

        print("Bolsistas: ", Bolsista.objects.all())
        print("Horarios do bolsista: ", HorarioBolsista.objects.filter(bolsista=1))

        return Bolsista.objects.filter(
            horariobolsista__dia_semana=dia_semana,
            horariobolsista__horario_inicio__lte=self.horario_pretendido,
            horariobolsista__horario_fim__gte=self.horario_pretendido,
        ).distinct()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        bolsistas = self.buscar_bolsista()
        print("Bolsistas disponíveis para o agendamento:")
        if bolsistas.exists():
            for b in bolsistas:
                print(f"✅ {b.nome} ({b.matricula}) - {b.curso}")
        else:
            print("Nenhum bolsista disponível no horário selecionado.")