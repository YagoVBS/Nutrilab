# Generated by Django 5.1.5 on 2025-02-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0002_dadospaciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospaciente',
            name='colesterol_hdl',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='dadospaciente',
            name='colesterol_ldl',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='dadospaciente',
            name='colesterol_total',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='dadospaciente',
            name='trigliceridios',
            field=models.IntegerField(blank=True),
        ),
    ]
