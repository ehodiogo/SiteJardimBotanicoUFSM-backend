# Generated by Django 5.2 on 2025-06-17 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amostras', '0003_amostra_localizacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amostra',
            options={'verbose_name': 'Amostra do Jardim Botânico', 'verbose_name_plural': 'Amostras do Jardim Botânico'},
        ),
        migrations.AlterModelOptions(
            name='dadoscientificos',
            options={'verbose_name': 'Dados Científicos da Amostra', 'verbose_name_plural': 'Dados Científicos das Amostras'},
        ),
    ]
