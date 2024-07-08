from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  logout
from .autenticacao import Autenticacao
from .forms import PlanejamentoForm
from .planejamentos import Planejamentos
from django.contrib.auth.decorators import login_required
import random



def movimentacoes(request): # VERIFICA SE O USER ESTA LOGADO // Redirecione para a página de login
    return render(request, 'movimentacoes/movimentacoes.html')

@login_required # VERIFICA SE O USER ESTA LOGADO // Redirecione para a página de login
def configuracoes(request):
    return render(request, 'configuracoes/configuracoes.html')

def perfil(request):
    if not request.user.is_authenticated:
        return redirect('login')  # VERIFICA SE O USER ESTA LOGADO // Redirecione para a página de login
    return render(request, 'home/home.html')

# ----------------------------------------------------------------------------------------------------------------------------- #
# PLANEJAMENTOS

# LISTAR PLANEJAMENTOS
@login_required # VERIFICA SE O USER ESTA LOGADO // Redirecione para a página de login
def planejamentos(request):
    planejamento_obj = Planejamentos(request.user)
    lista_planejamentos = planejamento_obj.listar_planejamentos()

    lista_vazia = not lista_planejamentos

    if lista_vazia:
        print('true')

    for planejamento in lista_planejamentos:
        planejamento.barra_iterable = range(planejamento.barra)

    return render(request, 'planejamentos/planejamentos.html', {'planejamentos': lista_planejamentos, 'verificaVazio': lista_vazia})

# NOVO PLANEJAMENTOS
@login_required # VERIFICA SE O USER ESTA LOGADO // Redirecione para a página de login
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

# EDIT PLANEJAMENTOS
@login_required # VERIFICA SE O USER ESTA LOGADO // Redirecione para a página de login
def editplanej(request):
    if request.method == 'POST':
        form = PlanejamentoForm(request.POST)
        planejamentos = Planejamentos(request.user)

    context = {
        'objetivo': '112312',
        'saldo_atual': '21312',
        'titulo': 'titulo teste',
        'data': '12/12/2012'
    }

    return render(request, 'planejamentos/editplanejamentos.html', context)

# ----------------------------------------------------------------------------------------------------------------------------- #
# HOME
def home(request):
    # Criado um dicionário com as duas chaves (frase e autor), assim conseguimos usar a biblioteca random para selecionar uma frase aleatoria
    frases = [
        {"frase": "Uma jornada de mil quilômetros precisa começar com um simples passo.", "autor": "Lao Tzu"},
        {"frase": "A riqueza é consequência de trabalho e poupança.", "autor": "Benjamin Franklin"},
        {"frase": "Jamais gaste seu dinheiro antes de você possuí-lo.", "autor": "Thomas Jefferson"},
        {"frase": "Sucesso é a soma de pequenos esforços, repetidos o tempo todo.", "autor": "Robert Collier"},
        {"frase": "Dinheiro é apenas uma ferramenta. Ele irá levá-lo onde quiser, mas não vai substituí-lo como motorista.", "autor": "Ayn Rand"},
        {"frase": "Cuidado com as pequenas despesas, um pequeno vazamento afundará um grande navio.", "autor": "Benjamin Franklin"},
        {"frase": "As pessoas gastam um dinheiro que não têm, para comprar coisas de que elas não precisam, para impressionar pessoas de quem não gostam.", "autor": "Will Rogers"},
    ]

    # Seleciona uma frase aleatoria
    frase_escolhida = random.choice(frases)

    # Aqui tem outro dicionario que usamos para passar as variaveis pra o HTML
    contexto = {
        "username": request.session.get('username', 'Visitante'),
        "frase": frase_escolhida["frase"],
        "autor": frase_escolhida["autor"]
    }
    return render(request, 'home/home.html', contexto)

def cadastro(request):
    cad = Autenticacao()
    return cad.cadastro(request)

def login(request):
    cad = Autenticacao()
    return cad.login(request)

def logout_view(request):
    logout(request)
    return render(request, 'login/login.html')  # Redirecione para a página de login ou outra página