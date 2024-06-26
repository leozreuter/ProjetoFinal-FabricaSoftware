from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def planejamentos(request):

    titulo = "TITULO"
    saldo_atual = 1000
    saldo_objetivo = 199999
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

def movimentacoes(request):
    return render(request, 'movimentacoes/movimentacoes.html')

def configuracoes(request):
    return render(request, 'configuracoes/configuracoes.html')

def perfil(request):
    return render(request, 'home/home.html')

def logout(request):
    return render(request, 'home/home.html')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first() or User.objects.filter(email=email).first()

        if user:
            return HttpResponse('Já existe usuário cadastrado com este usuário ou Email', status=409)
        
        novoUser = User.objects.create_user(username=username, email=email, password=senha)
        novoUser.save()

        return HttpResponse(f"Usuário {username} cadastrado com sucesso!", status=201)

def login(request):
    if request.method == 'GET':
       return render(request, 'login/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            #login(request, user)

            return HttpResponse('Autenticado com sucesso!', status=201)
        else:
            return HttpResponse('Usuario ou Senha inválidos')