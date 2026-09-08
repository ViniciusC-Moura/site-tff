from django.shortcuts import render, redirect, get_object_or_404
from .models import Esporte, Gestor, Jogo
from django.core.paginator import Paginator
from .filters import JogoFilter

def jogos(request):
    queryset = Jogo.objects.all().order_by('-data_hora')

    filterset = JogoFilter(request.GET, queryset=queryset)
    jogos_filtrados = filterset.qs

    paginator = Paginator(jogos_filtrados, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    filtros_ativos = {k: v for k, v in request.GET.items() if v and k != 'page'}

    context = {
        'filter': filterset,
        'jogos': page_obj,          # o template usa isso pra iterar
        'page_obj': page_obj,       # o template usa isso pra paginação
        'is_paginated': page_obj.has_other_pages(),
        'filtros_ativos': filtros_ativos,
    }
    return render(request, 'jogos.html', context)

def home(request):
    return render(request, 'home.html')

def sobre_nos(request):
    return render(request,'sobre_nos.html')

def gestao(request):
    gestores = Gestor.objects.all().order_by('funcao', 'nome')
    return render(request, 'gestao.html', {'gestores': gestores})

def equipes(request):
    esportes = Esporte.objects.all().order_by('nome')
    return render(request, 'equipes.html', {'esportes': esportes})
