# Generated by Django 2.0.2 on 2018-02-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180201_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cep',
            field=models.CharField(max_length=9, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=15, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rg',
            field=models.CharField(max_length=10, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telefone',
            field=models.CharField(max_length=11, verbose_name='Telefone'),
        ),
    ]
