from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class User(AbstractUser):

	username = models.CharField('Nome de Usuário', max_length=30, unique=True)
	email = models.EmailField('Email', unique=True)
	nome = models.CharField('Nome', max_length=40)
	portaria = models.CharField('Portaria', max_length=20, blank=True)
	matricula = models.CharField('Matrícula', max_length=10, blank=True)
	endereco = models.CharField('Endereço', max_length=50)
	cidade = models.CharField('Cidade', max_length=30)
	estado = models.CharField('Estado', max_length=20)
	cep = models.CharField('CEP', max_length=9)
	telefone = models.CharField('Telefone', max_length=11)
	cpf = models.CharField('CPF', max_length=15)
	rg = models.CharField('RG', max_length=10)
	is_pregoeiro = models.BooleanField('Pregoeiro', default=False)
	is_active = models.BooleanField('Ativo', blank=True, default=True)
	is_staff = models.BooleanField('Administrador', blank=True, default=False)

	objects = UserManager()
	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['nome', 'email']

	def __str__(self):
		return self.name or self.username

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return str(self)

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

