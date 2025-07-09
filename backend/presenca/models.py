from django.db import models

class Presenca(models.Model):

    agendamento = models.ForeignKey('agendamento.Agendamento', on_delete=models.CASCADE)
    visitante = models.CharField(max_length=255)

    def __str__(self):
        return self.visitante
    
    class Meta:
        verbose_name = 'Presença no Agendamento do Jardim Botânico'
        verbose_name_plural = 'Presenças no Agendamento do Jardim Botânico'