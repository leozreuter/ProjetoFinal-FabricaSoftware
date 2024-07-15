from pyexpat.errors import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

class Autenticacao:
    """
    Classe para lidar com a autenticação de usuários, incluindo cadastro e login.
    """

    def cadastro(self, request):
        
        """
        Gerencia o cadastro de novos usuários. Renderiza a página de cadastro em um 
        GET e cria um novo usuário em um POST.

        Args:
            request: A solicitação HTTP recebida.

        Returns:
            HttpResponse: A resposta HTTP contendo a página de cadastro ou redirecionamento para login.
        """

        if request.method == 'GET': #Se o metodo da requisição for GET renderiza a pagina em html
            return render(request, 'cadastro/cadastro.html')
        else: #Se o metodo for POST, ou seja o usuario esta enviando dados ele salva esses dados nas variaveis e cria um usuario
            username = request.POST.get('username')
            email = request.POST.get('email')
            senha = request.POST.get('senha')

            #Verifica se ja existe um usuario cadastrado no Banco de Dados com a mesmo nick e o mesmo e-mail
            user = User.objects.filter(username=username).first() or User.objects.filter(email=email).first()

            #Se existir (TRUE), então o cadastro falha e volta pra pagina principal de cadastro
            if user:
                cad_falho = True
                context = {
                    'cad_falho': cad_falho,
                }
                return render(request, 'cadastro/cadastro.html', context)
            
            #Se não existir vai ser criado um novo usuário e salvo no banco de dados
            novoUser = User.objects.create_user(username=username, email=email, password=senha)
            novoUser.save()

            return redirect('login')  #Redireciona para a a tela de login

    def login(self, request):
        """
        Gerencia o login dos usuários. Renderiza a página de login em um GET e autentica 
        o usuário em um POST.

        Args:
            request: A solicitação HTTP recebida.

        Returns:
            HttpResponse: A resposta HTTP contendo a página de login ou redirecionamento para a home.
        """

        if request.method == 'GET': #Se o metodo da requisição for GET renderiza a pagina em html
            return render(request, 'login/login.html')
        else: #Se o metodo for POST, ou seja o usuario esta enviando dados ele salva esses dados nas variaveis e faz o login do usuario
            username = request.POST.get('username')
            senha = request.POST.get('senha')

            user = authenticate(username=username, password=senha) #Autentica o usuário com os dados recebidos

            if user: #se der certo faz o login e salva o nome do usuario na sessão e o rediceciona para a pagina HOME
                login(request, user)
                request.session['username'] = username
                return redirect('home')
            else: #Se não da falha no login e renderiza a pagina de login novamente para ele tentar outra
                login_falho = True
                context = {
                    'login_falho': login_falho,
                }
                return render(request, 'login/login.html', context)