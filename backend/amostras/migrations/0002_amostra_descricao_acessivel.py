# Generated by Django 5.2 on 2025-04-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amostras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amostra',
            name='descricao_acessivel',
            field=models.TextField(blank=True, null=True),
        ),
    ]
