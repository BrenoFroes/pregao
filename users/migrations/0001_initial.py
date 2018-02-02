# Generated by Django 2.0.2 on 2018-02-01 19:17

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Nome de Usuário')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('portaria', models.CharField(blank=True, max_length=20, verbose_name='Portaria')),
                ('matricula', models.CharField(blank=True, max_length=10, verbose_name='Matrícula')),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
                ('cep', models.IntegerField(verbose_name='CEP')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('cpf', models.IntegerField(verbose_name='CPF')),
                ('rg', models.IntegerField(verbose_name='RG')),
                ('is_pregoeiro', models.BooleanField(default=False, verbose_name='Pregoeiro')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Administrador')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
