from django.urls import path

from . import views

app_name = 'fornecedores'
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
]