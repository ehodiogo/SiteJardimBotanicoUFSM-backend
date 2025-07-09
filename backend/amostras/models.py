from django.db import models
from django.db.models import TextChoices

class DadosCientificos(models.Model):
    nome_cientifico = models.CharField(max_length=255, blank=True, null=True)
    reino = models.CharField(max_length=255, blank=True, null=True)
    filo = models.CharField(max_length=255, blank=True, null=True)  
    classe = models.CharField(max_length=255, blank=True, null=True)
    ordem = models.CharField(max_length=255, blank=True, null=True)
    familia = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=255, blank=True, null=True)
    especie = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome_cientifico
    
    class Meta:
        verbose_name = 'Dados Científicos da Amostra'
        verbose_name_plural = 'Dados Científicos das Amostras'

class AmostraType(TextChoices):
    PLANTA = 'planta', 'Planta'
    FUNGO = 'fungo', 'Fungo'
    ANIMAL = 'animal', 'Animal'

class Amostra(models.Model):
    nome_cientifico = models.CharField(max_length=255)
    nome_popular = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    descricao_acessivel = models.TextField(blank=True, null=True)
    tipo = models.CharField(
        max_length=10, 
        choices=AmostraType.choices, 
        default=AmostraType.PLANTA
    )
    origem = models.CharField(max_length=255, blank=True, null=True)
    data_registro = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='amostras/', blank=True, null=True)
    imagem_url = models.CharField(max_length=300, null=True, blank=True)

    dados_cientificos = models.ForeignKey('DadosCientificos', on_delete=models.CASCADE)

    # could have loc
    localizacao = models.ForeignKey('trilhas.Ponto', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nome_popular or self.nome_cientifico} ({self.get_tipo_display()})"

    class Meta:
        verbose_name = 'Amostra do Jardim Botânico'
        verbose_name_plural = 'Amostras do Jardim Botânico'