from django.db import models
from core.models import Pregao
from fornecedores.models import Fornecedor

class Historico(models.Model):
	pregao = models.ForeignKey(Pregao, on_delete=models.CASCADE)
