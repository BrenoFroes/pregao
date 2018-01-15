from django.urls import path
from . import views

urlpatterns = [
	path('cadastrarpregoeiro/', views.cadastrarpregoeiro, name='cadastrarpregoeiro'),
]