from django.db import models

class QuizAmostra(models.Model):
    amostra = models.ForeignKey('amostras.Amostra', on_delete=models.CASCADE)
    
    pergunta = models.CharField(max_length=255)
    resposta_correta = models.CharField(max_length=255)
    resposta_incorreta_1 = models.CharField(max_length=255)
    resposta_incorreta_2 = models.CharField(max_length=255)

    def __str__(self):
        return self.pergunta
    
    class Meta:
        verbose_name = 'Pergunta do Quiz do Jardim Botânico'
        verbose_name_plural = 'Perguntas do Quiz do Jardim Botânico'