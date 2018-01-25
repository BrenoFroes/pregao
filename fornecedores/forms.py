from django import forms

MICROEMPRESAOPCOES = (('SIM', 'Sim',), ('NAO', 'Não',))
ESTADOS = (
		('AC', 'Acre'),
		('AL', 'Alagoas'),
		('AP', 'Amapá'),
		('AM', 'Amazonas'),
		('BA', 'Bahia'),
		('CE', 'Ceará'),
		('DF', 'Distrito Federal'),
		('ES', 'Espírito Santo'),
		('GO', 'Goiás'),
		('MA', 'Maranhão'),
		('MT', 'Mato Grosso'),
		('MS', 'Mato Grosso do Sul'),
		('MG', 'Minas Gerais'),
		('PA', 'Pará'),
		('PB', 'Paraíba'),
		('PR', 'Paraná'),
		('PE', 'Pernambuco'),
		('PI', 'Piauí'),
		('RJ', 'Rio de Janeiro'),
		('RN', 'Rio Grande do Norte'),
		('RS', 'Rio Grande do Sul'),
		('RO', 'Rondônia'),
		('RR', 'Roraima'),
		('SC', 'Santa Catarina'),
		('SP', 'São Paulo'),
		('SE', 'Sergipe'),
		('TO', 'Tocantins'),
		)


class FornecedoresForm(forms.Form):

	cnpj = forms.CharField(label='CNPj', max_length=100)
	inscricaoestadual = forms.CharField(label='Inscrição Estadual', max_length=100)
	razaosocial = forms.CharField(label='Razão Social', max_length=100)
	nomefantasia = 	forms.CharField(label='Nome Fantasia', max_length=100)
	email = forms.EmailField(label='Email')
	telefone = forms.CharField(label='Telefone', max_length=11)
	endereco = forms.CharField(label='Endereco', max_length=100)
	cep = forms.CharField(label='CEP', max_length=8)
	estado = forms.CharField(label='Estado', max_length=100, widget=forms.Select(choices=ESTADOS))
	cidade = forms.CharField(label='Cidade', max_length=100)
	microempresa = forms.ChoiceField(label='Micro-Empresa', widget=forms.RadioSelect, choices=MICROEMPRESAOPCOES)