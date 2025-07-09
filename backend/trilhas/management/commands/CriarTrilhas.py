from django.core.management.base import BaseCommand
from trilhas.models import GuiaTrilha, Ponto, Trilha
from tag.models import Tag 


class Command(BaseCommand):
    help = "Popula o banco de dados com dados de exemplo para testes"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Iniciando a população do banco..."))

        guia = GuiaTrilha.objects.create(descricao="Aqui você está no hall de entrada do Jardim Botânico. Há uma grande porta de vidro à sua esquerda e ao entrar no Hall, haverão inúmeros animais empalados.")

        ponto1 = Ponto.objects.create(
            latitude=-29.716910418059822,
            longitude=-53.72960880114982,
            descricao="Hall de Entrada",
            guia=guia,
            order=1,
        )

        guia2 = GuiaTrilha.objects.create(descricao="Aqui você está entrando na área do Jardim Botânico. Aqui o chão é de grama e ao ar livre. À sua direita existem diversas árvores nativas e à sua esquerda também.")

        ponto2 = Ponto.objects.create(
            latitude=-29.71708692014737,
            longitude=-53.729620183519536,
            descricao="Passagem pelo Hall de Entrada",
            guia=guia2,
            order=2,
        )

        guia3 = GuiaTrilha.objects.create(descricao="Nesse ponto você encontra uma roda de bancos de diversas cores, vermelho, amarelo, verde, entre outros. A roda de banco está cercada de diversas árvores e à sua direita existe uma escada que permite que você suba ao telhado verde.")

        ponto3 = Ponto.objects.create(
            latitude=-29.717072218734508,
            longitude=-53.729796917318055,
            descricao="Chegada à roda de bancos",
            guia=guia3,
            order=3,
        )

        tag1 = Tag.objects.create(tag="Fácil")
        tag2 = Tag.objects.create(tag="Plantas")
        tag3 = Tag.objects.create(tag="Ar Livre")

        trilha = Trilha.objects.create(nome="Trilha Simples", duracao="15 min", dificuldade=1)
        trilha.pontos.set([ponto1, ponto2, ponto3])
        trilha.tags.set([tag1, tag2, tag3])

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
