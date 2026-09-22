from django.shortcuts import render, redirect, get_object_or_404
from .models import Esporte, Gestor, Jogo, Noticia, Evento, Foto
from django.core.paginator import Paginator
from .filters import JogoFilter

def jogos(request):
    # ==========================================
    # 1. LÓGICA DOS JOGOS
    # ==========================================
    queryset = Jogo.objects.all().order_by('-data_hora')

    filterset = JogoFilter(request.GET, queryset=queryset)
    jogos_filtrados = filterset.qs

    paginator = Paginator(jogos_filtrados, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    filtros_ativos = {k: v for k, v in request.GET.items() if v and k != 'page'}

    # ==========================================
    # 2. LÓGICA DAS FOTOS (CORRIGIDA)
    # ==========================================
    fotos = Foto.objects.all().order_by('-id')

    # Capturando os parâmetros que vêm da URL (?competicao=intercampi&edicao=...)
    competicao = request.GET.get('competicao')
    edicao = request.GET.get('edicao')
    fase_competicao = request.GET.get('fase_competicao')
    modalidade = request.GET.get('modalidade') or request.GET.get('esporte')

    # Aplica os filtros na Foto apenas se o parâmetro não estiver vazio
    if competicao:
        fotos = fotos.filter(competicao=competicao)  # Corrigido: sem _id

    if edicao:
        fotos = fotos.filter(edicao=edicao)

    if fase_competicao:
        fotos = fotos.filter(fase_competicao=fase_competicao)

    if modalidade:
        fotos = fotos.filter(esporte_id=modalidade)

    # Limita em no máximo 12 fotos para o carrossel
    fotos = fotos[:12]

    # ==========================================
    # 3. CONTEXTO
    # ==========================================
    context = {
        'filter': filterset,
        'jogos': page_obj,          
        'page_obj': page_obj,       
        'is_paginated': page_obj.has_other_pages(),
        'filtros_ativos': filtros_ativos,
        'fotos': fotos,             
    }
    
    return render(request, 'jogos.html', context)

def home(request):
    noticias = Noticia.objects.all().order_by('-data')

    proximos_jogos = Jogo.objects.filter(status='marcado').order_by('data_hora')[:4]
    ultimos_jogos = Jogo.objects.filter(status='finalizado').order_by('-data_hora')[:4]

    context = {
        'noticias': noticias,
        'ultimos_jogos': ultimos_jogos,
        'proximos_jogos': proximos_jogos,
    }

    return render(request, 'home.html', context)

def sobre_nos(request):
    return render(request,'sobre_nos.html')

def gestao(request):
    gestores = Gestor.objects.all().order_by('funcao', 'nome')
    return render(request, 'gestao.html', {'gestores': gestores})

def equipes(request):
    esportes = Esporte.objects.all().order_by('nome')
    return render(request, 'equipes.html', {'esportes': esportes})

def equipe(request, nome_esporte):
    esporte = get_object_or_404(Esporte, slug=nome_esporte)
    return render(request, 'equipe.html', {'esporte': esporte})
def noticias(request):
    noticias = Noticia.objects.all().order_by('-data')
    context = {
            'noticias': noticias,
        }
    return render(request, 'noticias.html', context)

def eventos(request):
    eventos = Evento.objects.all().order_by('-data_hora')
    return render(request, 'eventos.html', {'eventos': eventos,})


