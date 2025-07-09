from django.db import models

class ConfiguracaoJB(models.Model):
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()

    dia_semana = models.IntegerField()

    def __str__(self):
        return f"{self.dia_semana} - {self.horario_abertura} - {self.horario_fechamento}"

    class Meta:
        verbose_name = 'Configuração de Horário de Funcionamento do Jardim Botânico'
        verbose_name_plural = 'Configurações de Horário de Funcionamento do Jardim Botânico'
