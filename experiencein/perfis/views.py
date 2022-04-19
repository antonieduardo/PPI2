from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request): 
    return render(request, 'index.html')

def exibir(request, perfil_id):
    print('ID do perfil recebido: {}'.format(perfil_id))
    return render(request, 'perfil.html')