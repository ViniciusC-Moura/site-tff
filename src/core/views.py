from django.shortcuts import render, redirect, get_object_or_404
from .models import Esporte, Gestor

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
