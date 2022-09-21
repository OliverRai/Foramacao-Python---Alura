from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

# Create your views here.

def index(request):
    receitas = Receita.objects.flter(publicada = True)
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