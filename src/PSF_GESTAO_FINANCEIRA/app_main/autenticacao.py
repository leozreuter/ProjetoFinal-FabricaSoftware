from pyexpat.errors import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

class Autenticacao:

    def cadastro(self, request):
        if request.method == 'GET':
            return render(request, 'cadastro/cadastro.html')
        else:
            username = request.POST.get('username')
            email = request.POST.get('email')
            senha = request.POST.get('senha')

            user = User.objects.filter(username=username).first() or User.objects.filter(email=email).first()

            if user:
                cad_falho = True
                context = {
                    'cad_falho': cad_falho,
                }
                return render(request, 'cadastro/cadastro.html', context)
            
            novoUser = User.objects.create_user(username=username, email=email, password=senha)
            novoUser.save()

            return redirect('login')  #Redireciona para a a tela de login

    def login(self, request):
        if request.method == 'GET':
            return render(request, 'login/login.html')
        else:
            username = request.POST.get('username')
            senha = request.POST.get('senha')

            user = authenticate(username=username, password=senha)

            if user:
                login(request, user)
                request.session['username'] = username
                return redirect('home')
            else:
                login_falho = True
                context = {
                    'login_falho': login_falho,
                }
                return render(request, 'login/login.html', context)