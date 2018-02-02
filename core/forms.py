from django import forms

class Pregao(forms.Form):
	modalidade = forms.CharField('Modalidade', max_length=20)
	numero = forms.CharField('Nº do Pregão', max_length=100)
	numeroProcesso = forms.CharField('Nº do Processo', max_length=100)
	objeto = forms.CharField('Objeto', max_length=1000)
	valorEstimado = forms.DecimalField('Valor Estimado', max_digits=17, decimal_places=2)
	pregoeiro = forms.CharField('Pregoeiro', max_length=100)
	equipeDeApoio = forms.CharField('Equipe de Apoio', max_length=300)

class Item(forms.Form):
	objeto = forms.CharField('Objeto', max_length=1000)
	numero = forms.IntegerField('Número do ítem')
	valorUnitario = forms.DecimalField('Valor Unitário', max_digits=17, decimal_places=2)
	quantidade = forms.IntegerField('Quantidade do Item')
	unidade = forms.CharField('Unidade', max_length=100)