from django.db import models

class UsersManager(models.Manager):
	def search(self, query):
		return self.get_queryset.filter(models.Q(nome__icontains=query | models.Q(matricula__icontains=query)))


class Users(models.Model):

	nome = models.CharField('Nome', max_length=100)
	senha = models.CharField('Senha', max_length=10)
	matricula = models.CharField('Matricula', max_length=10)
	portaria = models.CharField('Portaria', max_length=20)
	endereco = models.CharField('Endereço', max_length=100)
	cidade = models.CharField('Cidade', max_length=20)
	cep = models.CharField('CEP',max_length=9)
	estado = models.CharField('Estado', max_length=20)
	telefone = models.CharField('Telefone', max_length=12)
	email = models.EmailField('Email')
	cpf = models.CharField('CPF', max_length=14)
	rg = models.CharField('RG', max_length=8)

