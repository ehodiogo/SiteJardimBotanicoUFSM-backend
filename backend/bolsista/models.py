from django.db import models

class Bolsista(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    matricula = models.CharField(max_length=25, unique=True)
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=10)

    def __str__(self):
        return self.matricula + " - " + self.curso + " - " + self.nome

    class Meta:
        verbose_name = 'Bolsista do Jardim Botânico'
        verbose_name_plural = 'Bolsistas do Jardim Botânico'

class HorarioBolsista(models.Model):
    DIAS_SEMANA = (
        (0, "Segunda-feira"),
        (1, "Terça-feira"),
        (2, "Quarta-feira"),
        (3, "Quinta-feira"),
        (4, "Sexta-feira"),
        (5, "Sábado"),
        (6, "Domingo"),
    )

    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE)
    dia_semana = models.IntegerField(choices=DIAS_SEMANA)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def __str__(self):
        dia = dict(self.DIAS_SEMANA).get(self.dia_semana, "Desconhecido")
        return f"{self.bolsista} - {dia} - {self.horario_inicio} às {self.horario_fim}"

    class Meta:
        verbose_name = "Horário do Bolsista do Jardim Botânico"
        verbose_name_plural = "Horários do Bolsista do Jardim Botânico"


# dia semana = 6 - domingo
# dia semana = 0 - segunda
# dia semana = 1 - terca
# dia semana = 2 - quarta
# dia semana = 3 - quinta
# dia semana = 4 - sexta
# dia semana = 5 - sabado
