from django.shortcuts import render
from django.http import HttpResponse

def cadastrarpregoeiro(request):
	return render(request, 'cadastrarpregoeiro.html')