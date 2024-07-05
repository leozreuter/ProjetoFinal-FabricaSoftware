from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  logout
from .autenticacao import Autenticacao
from .forms import PlanejamentoForm
from .planejamentos import Planejamentos
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    username = request.session.get('username', 'visitante')
    return render(request, 'home/home.html',{'username': username})

@login_required
def planejamentos(request):
    planejamento_obj = Planejamentos(request.user)
    lista_planejamentos = planejamento_obj.listar_planejamentos()

    for planejamento in lista_planejamentos:
        planejamento.barra_iterable = range(planejamento.barra)

    return render(request, 'planejamentos/planejamentos.html', {'planejamentos': lista_planejamentos})

    """
    titulo = "TITULO"
    saldo_atual = 50
    saldo_objetivo = 100
    concluido = False

    barra = (saldo_atual * 100) // saldo_objetivo

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
    """

def movimentacoes(request):
    return render(request, 'movimentacoes/movimentacoes.html')

@login_required
def newplanejamento(request):
    if request.method == 'POST':
        form = PlanejamentoForm(request.POST)
        planejamentos = Planejamentos(request.user)
        if planejamentos.criar_planejamento(form):
            return redirect('planejamentos')
        else:
            print(form.errors)
    else:
        form = PlanejamentoForm()
    return render(request, 'planejamentos/novoplanejamento.html', {'form': form})

def configuracoes(request):
    return render(request, 'configuracoes/configuracoes.html')

def perfil(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirecione para a página de login
    return render(request, 'home/home.html')

def cadastro(request):
    cad = Autenticacao()
    return cad.cadastro(request)

def login(request):
    cad = Autenticacao()
    return cad.login(request)

@login_required
def editplanej(request):
    return render(request, 'planejamentos/editplanejamentos.html')

def logout_view(request):
    logout(request)
    return render(request, 'login/login.html')  # Redirecione para a página de login ou outra página