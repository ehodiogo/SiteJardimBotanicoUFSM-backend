from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag
    
    class Meta:
        verbose_name = 'Tag das Trilhas e Amostras do Jardim Botânico'
        verbose_name_plural = 'Tags das Trilhas e Amostras do Jardim Botânico'