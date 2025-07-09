from django.db import models

class Ponto(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    descricao = models.TextField(blank=True, null=True)

    # could have
    guia = models.ForeignKey('GuiaTrilha', on_delete=models.SET_NULL, null=True, blank=True)

    # could have 
    order = models.IntegerField(blank=True, null=True)

    # imagem
    imagem = models.ImageField(upload_to='trilhas/', blank=True, null=True)

    def __str__(self):
        return f"{self.latitude}, {self.longitude} - {self.descricao} - {self.guia} - {self.order}"
    
    class Meta:
        verbose_name = 'Ponto da Trilha do Jardim Botânico'
        verbose_name_plural = 'Pontos da Trilha do Jardim Botânico'

class GuiaTrilha(models.Model):
    descricao = models.TextField(blank=True, null=True)
    proximo_passo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Guia de Trilha do Jardim Botânico'
        verbose_name_plural = 'Guias de Trilhas do Jardim Botânico'


class Trilha(models.Model):

    DIFICULDADES = (
        (1, "Fácil"),
        (2, "Médio"),
        (3, "Difícil")
    )
    nome = models.CharField(max_length=150)
    pontos = models.ManyToManyField(Ponto)
    duracao = models.PositiveSmallIntegerField(blank=True, null=True)
    dificuldade = models.PositiveSmallIntegerField(blank=True, null=True, choices=DIFICULDADES)

    # tags da trilha
    tags = models.ManyToManyField('tag.Tag')

    def __str__(self):
        dificuldade = dict(self.DIFICULDADES).get(self.dificuldade, "Desconhecido")
        return f"{self.nome} - {dificuldade} + {self.duracao} minutos de trilha"

    class Meta:
        verbose_name = 'Trilha Guiada do Jardim Botânico'
        verbose_name_plural = 'Trilhas Guiadas do Jardim Botânico'
