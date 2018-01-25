from django.shortcuts import render
from django.http import HttpResponse
from .forms import FornecedoresForm
from django.http import HttpResponseRedirect
from .models import Fornecedor

def cadastro(request):
	form = FornecedoresForm()
	if request.method == 'POST':
		form = FornecedoresForm(request.POST)
		if form.is_valid():
			dados = form.cleaned_data
			fornecedor = Fornecedor(cnpj=dados['cnpj'], inscricaoestadual=dados['inscricaoestadual'],
				razaosocial=dados['razaosocial'], nomefantasia=dados['nomefantasia'], email=dados['email'],
				telefone=dados['telefone'], endereco=dados['endereco'], cep=dados['cep'], estado=dados['estado'],
				cidade=dados['cidade'], microempresa=dados['microempresa'])
			fornecedor.save()
			return HttpResponseRedirect("")
		else:
			form = FornecedoresForm()

	return render(request, 'cadastro.html', {'form': form})

