from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .autenticacao import Autenticacao

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def planejamentos(request):

    titulo = "TITULO"
    saldo_atual = 50
    saldo_objetivo = 100
    concluido = False

    barra = (saldo_atual * 100) // saldo_objetivo
    print(barra)

    if barra >= 100:
        barra = 100
        concluido = True

    context = {
        'range': range(3),
        'titulo': titulo,
        'saldo_objetivo': saldo_objetivo,
        'data': '12/12/2012',
        'insvest_mes': '123,45',
        'saldo_atual': saldo_atual,
        'barra': range(barra),
        'concluido': concluido
    }


    return render(request, 'planejamentos/planejamentos.html', context)

def movimentacoes(request):
    return render(request, 'movimentacoes/movimentacoes.html')

def configuracoes(request):
    return render(request, 'configuracoes/configuracoes.html')

def perfil(request):
    return render(request, 'home/home.html')

def logout(request):
    return render(request, 'home/home.html')

def cadastro(request):
    cad = Autenticacao()
    return cad.cadastro(request)

def login(request):
    cad = Autenticacao()
    return cad.login(request)
        
def editplanej(request):
    return render(request, 'planejamentos/editplanejamentos.html')