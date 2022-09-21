from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

# Create your views here.

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada = True)
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):

    receita = get_object_or_404(Receita, pk=receita_id)

    receita = {
        'receita' : receita
    }

    return render(request, 'receita.html', receita)

def buscar(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada = True)

    if 'buscar' in request.GET:
        nome_a_receita = request.GET['buscar']  

        if nome_a_receita:
            lista = receitas.filter(nome_receita__icontains=nome_a_receita)

    dados = {
        'receitas': lista
    }
    return render(request, 'buscar.html', dados)
