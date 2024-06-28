from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse

class Autenticacao:

    #@staticmethod
    def cadastro(self, request):
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

            return redirect('login')  #Redireciona para a a tela de login



    #@staticmethod  
    def login(self, request):
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