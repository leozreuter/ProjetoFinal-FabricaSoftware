from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from .planejamentos import Planejamentos
from .autenticacao import Autenticacao
from django.http import HttpResponse
from django.contrib import messages
from .forms import PlanejamentoForm
import random
from.models import Planejamento

def movimentacoes(request):
    """
    Renderiza a página de movimentações.

    Parametros:
        request: A solicitação HTTP recebida.

    Returns:
        HttpResponse: A resposta HTTP contendo a página de movimentações.
    """
    return render(request, 'movimentacoes/movimentacoes.html')

@login_required
def configuracoes(request):
    """
    Renderiza a página de configurações. Verifica se o usuário está logado.

    Parametros:
        request: A solicitação HTTP recebida.

    Returns:
        HttpResponse: A resposta HTTP contendo a página de configurações.
    """
    return render(request, 'configuracoes/configuracoes.html')



def perfil(request):
    """
    Renderiza a página de perfil. Se o usuário não estiver autenticado, redireciona para a página de login.

    Parametros:
        request: A solicitação HTTP recebida.

    Returns:
        HttpResponse: A resposta HTTP contendo a página de perfil ou redirecionamento para a página de login.
    """

    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'username': request.user.username,
        'email': request.user.email,
        'id': request.user.id
    }

    return render(request, 'perfil/perfil.html', context)

# ----------------------------------------------------------------------------------------------------------------------------- #
# PLANEJAMENTOS

@login_required
def planejamentos(request):
    """
    Lista os planejamentos do usuário logado.

    Parametros:
        request: A solicitação HTTP recebida.

    Returns:
        HttpResponse: A resposta HTTP contendo a lista de planejamentos ou uma mensagem indicando que a lista está vazia.
    """
    planejamento_obj = Planejamentos(request.user)
    lista_planejamentos = planejamento_obj.listar_planejamentos()
    lista_vazia = not lista_planejamentos

    for planejamento in lista_planejamentos:
        planejamento.barra_iterable = range(planejamento.barra)

    print(lista_planejamentos)

    return render(request, 'planejamentos/planejamentos.html', {'planejamentos': lista_planejamentos, 'verificaVazio': lista_vazia})

@login_required
def newplanejamento(request):
    """
    Cria um novo planejamento. Se o método de solicitação for POST, tenta criar um planejamento com os dados do formulário.

    Parametros:
        request: A solicitação HTTP recebida.

    Returns:
        HttpResponse: A resposta HTTP contendo o formulário para criar um novo planejamento ou redirecionamento para a lista de planejamentos.
    """
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

@login_required
def editplanej(request, planejamento_id):
    """
    View para editar um planejamento específico.

    Obtém o planejamento correspondente ao planejamento_id para o usuário autenticado.
    Se o método da requisição for POST, tenta editar o planejamento com os dados do formulário.
    Se a edição for bem-sucedida, redireciona para a página de planejamentos.
    Caso contrário, exibe uma mensagem de erro e renderiza o formulário novamente.

    Parametros:
        request (HttpRequest): A requisição HTTP recebida.
        planejamento_id (int): O ID do planejamento a ser editado.

    Returns:
        HttpResponse: Redireciona para a página de planejamentos ou renderiza a página de edição.
    """

   #Obtenha o planejamento ou retorne um erro 404 se não existir
    planejamento = get_object_or_404(Planejamento, id=planejamento_id, usuario=request.user)
    planejamentos = Planejamentos(request.user)
    
    if request.method == 'POST':
        #Se o método da requisição for POST, significa que o usuário confirmou a edição
        form = PlanejamentoForm(request.POST, instance=planejamento)
        if form.is_valid():
            #Tente editar o planejamento
            if planejamentos.editar_planejamento(planejamento_id, form):
                #Redirecione para a página de planejamentos após a edição
                return redirect('planejamentos')
            else:
                #Exibe uma mensagem de erro se a edição falhar
                messages.error(request, 'Houve um problema ao salvar o planejamento. Verifique os dados e tente novamente.')
    else:
        #Se não for POST, preencha o formulário com os dados atuais do planejamento
        form = PlanejamentoForm(instance=planejamento)

    context = {
        'form': form,
        'planejamento': planejamento,
    }

    return render(request, 'planejamentos/editplanejamentos.html', context)


def excluirplanej(request, planejamento_id):
    """
    View para excluir um planejamento específico.

    Obtém o planejamento correspondente ao planejamento_id para o usuário autenticado.
    Se o método da requisição for POST, exclui o planejamento.
    Redireciona para a página de planejamentos após a exclusão.

    Parametros:
        request (HttpRequest): A requisição HTTP recebida.
        planejamento_id (int): O ID do planejamento a ser excluído.

    Returns:
        HttpResponse: Redireciona para a página de planejamentos ou renderiza a página de planejamentos.
    """
    #Obtenha o planejamento ou retorne um erro 404 se não existir
    planejamento = get_object_or_404(Planejamento, id=planejamento_id, usuario=request.user)

    if request.method == 'POST':
        #Se o método da requisição for POST, significa que o usuário confirmou a exclusão
        planejamento.delete()  #Exclua o planejamento do banco de dados
        return redirect('planejamentos')  #Redirecione para a página de planejamentos após a exclusão

    #Se não for POST, volta para a aba de planejamentos
    return render(request, 'planejamentos/planejamentos.html', {'planejamento': planejamento})

# ----------------------------------------------------------------------------------------------------------------------------- #
# HOME

def home(request):
    """
    Renderiza a página inicial com uma frase motivacional aleatória.

    Parametros:
        request: A solicitação HTTP recebida.

    Returns:
        HttpResponse: A resposta HTTP contendo a página inicial com uma frase motivacional aleatória.
    """
    frases = [
        {"frase": "Uma jornada de mil quilômetros precisa começar com um simples passo.", "autor": "Lao Tzu"},
        {"frase": "A riqueza é consequência de trabalho e poupança.", "autor": "Benjamin Franklin"},
        {"frase": "Jamais gaste seu dinheiro antes de você possuí-lo.", "autor": "Thomas Jefferson"},
        {"frase": "Sucesso é a soma de pequenos esforços, repetidos o tempo todo.", "autor": "Robert Collier"},
        {"frase": "Dinheiro é apenas uma ferramenta. Ele irá levá-lo onde quiser, mas não vai substituí-lo como motorista.", "autor": "Ayn Rand"},
        {"frase": "Cuidado com as pequenas despesas, um pequeno vazamento afundará um grande navio.", "autor": "Benjamin Franklin"},
        {"frase": "As pessoas gastam um dinheiro que não têm, para comprar coisas de que elas não precisam, para impressionar pessoas de quem não gostam.", "autor": "Will Rogers"},
        {"frase": "A educação formal vai fazer você ganhar a vida. A autoeducação vai fazer você alcançar uma fortuna.", "autor": "Jim Rohn"},
        {"frase": "O único lugar em que sucesso vem antes de trabalho é no dicionário.", "autor": "Vidal Sassoon"},
        {"frase": "Dinheiro é um mestre terrível, mas um excelente servo.", "autor": "P. T. Barnum"},
        {"frase": "A maneira mais rápida de ganhar dinheiro é resolver um problema. Quanto maior for o problema a resolver, mais dinheiro que você vai ganhar.", "autor": "Steve Siebold"},
    ]

    frase_escolhida = random.choice(frases)

    contexto = {
        "username": request.session.get('username', 'Visitante'),
        "frase": frase_escolhida["frase"],
        "autor": frase_escolhida["autor"]
    }
    return render(request, 'home/home.html', contexto)

def cadastro(request):
    """
    Renderiza a página de cadastro e realiza o processo de cadastro de usuário.

    Parametros:
        request: A solicitação HTTP recebida.

    Returns:
        HttpResponse: A resposta HTTP contendo a página de cadastro.
    """
    cad = Autenticacao()
    return cad.cadastro(request)

def login(request):
    """
    Renderiza a página de login e realiza o processo de autenticação do usuário.

    Parametros:
        request: A solicitação HTTP recebida.

    Returns:
        HttpResponse: A resposta HTTP contendo a página de login.
    """
    cad = Autenticacao()
    return cad.login(request)

def logout_view(request):
    """
    Realiza o logout do usuário e redireciona para a página de login.

    Parametros:
        request: A solicitação HTTP recebida.

    Returns:
        HttpResponse: A resposta HTTP contendo a página de login após o logout.
    """
    logout(request)
    return render(request, 'login/login.html')