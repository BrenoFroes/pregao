from django.db import models
from fornecedores.models import Fornecedor

class PregaoManager(models.Manager):
	def search (self, query):
		return self.get_queryset().filter(models.Q(numero__icontains=query) | 
			models.Q(objeto__icontains=query) | models.Q(numeroProcesso__icontains=query))

class Pregao(models.Model):
	modalidade = models.CharField('Modalidade', max_length=20)
	numero = models.CharField('Nº do Pregão', max_length=100)
	numeroProcesso = models.CharField('Nº do Processo', max_length=100)
	objeto = models.CharField('Objeto', max_length=1000)
	valorEstimado = models.DecimalField('Valor Estimado', max_digits=17, decimal_places=2)
	pregoeiro = models.CharField('Pregoeiro', max_length=100)
	equipeDeApoio = models.CharField('Equipe de Apoio', max_length=300)

	objects = PregaoManager()

	def __str__(self):
		return self.numero

class ItemManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(models.Q(objeto__icontains=query))

class Item(models.Model):
	objeto = models.CharField('Objeto', max_length=1000)
	numero = models.IntegerField('Número do ítem')
	valorUnitario = models.DecimalField('Valor Unitário', max_digits=17, decimal_places=2)
	quantidade = models.IntegerField('Quantidade do Item')
	unidade = models.CharField('Unidade', max_length=100)

	objects = ItemManager

	def __str__(self):
		return self.objeto

class ItemDoPregao(models.Model):
	pregao = models.ForeignKey(Pregao, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	preco = models.DecimalField('Preço Inicial', max_digits=17, decimal_places=2)

	def __str__(self):
		item = self.item
		return item.objeto

class Proposta(models.Model):
	itemDoPregao = models.ForeignKey(ItemDoPregao, on_delete=models.CASCADE)
	fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
	valor = models.DecimalField('Valor da Proposta', max_digits=17, decimal_places=2)

	def __str__(self):
		item = self.ItemDoPregao.Item.objeto
		fornecedor = self.fornecedor
		valor = str(self.valor)
		saida = item + " " + fornecedor + " " + valor
		return saida

class Lance(models.Model):
	itemDoPregao = models.ForeignKey(ItemDoPregao, on_delete=models.CASCADE)
	fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
	valor = models.DecimalField('Valor do Lance', max_digits=17, decimal_places=2)

	def __str__(self):
		item = self.ItemDoPregao.Item.objeto
		fornecedor = self.fornecedor
		valor = str(self.valor)
		saida = item + " " + fornecedor + " " + valor
		return saida