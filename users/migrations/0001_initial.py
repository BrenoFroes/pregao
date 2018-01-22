# Generated by Django 2.0.1 on 2018-01-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('senha', models.CharField(max_length=10, verbose_name='Senha')),
                ('matricula', models.CharField(max_length=10, verbose_name='Matricula')),
                ('portaria', models.CharField(max_length=20, verbose_name='Portaria')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=20, verbose_name='Cidade')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
                ('telefone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('rg', models.CharField(max_length=8, verbose_name='RG')),
            ],
        ),
    ]
