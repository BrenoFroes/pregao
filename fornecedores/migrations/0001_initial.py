# Generated by Django 2.0.2 on 2018-02-02 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=100, verbose_name='CNPj')),
                ('inscricaoestadual', models.CharField(max_length=100, verbose_name='Inscrição Estadual')),
                ('razaosocial', models.CharField(max_length=100, verbose_name='Razão Social')),
                ('nomefantasia', models.CharField(max_length=100, verbose_name='Nome Fantasia')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereco')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('microempresa', models.CharField(max_length=3, verbose_name='Micro-Empresa')),
            ],
        ),
    ]
