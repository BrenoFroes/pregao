from django.db import models

class FornecedorManager(models.Manager):
	def search (self, query):
		return self.get_queryset().filter(models.Q(nomefantasia__icontains=query) | models.Q(cnpj__icontains=query))

class Fornecedor(models.Model):
	cnpj = models.CharField('CNPj', max_length=100)
	inscricaoestadual = models.CharField('Inscrição Estadual', max_length=100)
	razaosocial = models.CharField('Razão Social', max_length=100)
	nomefantasia = 	models.CharField('Nome Fantasia', max_length=100)
	email = models.EmailField('Email')
	telefone = models.CharField('Telefone', max_length=11)
	endereco = models.CharField('Endereco', max_length=100)
	cep = models.CharField('CEP', max_length=8)
	estado = models.CharField('Estado', max_length=100)
	cidade = models.CharField('Cidade', max_length=100)
	microempresa = models.CharField('Micro-Empresa', max_length=100)

