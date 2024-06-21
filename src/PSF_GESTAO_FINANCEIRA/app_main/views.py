from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home\home.html')

def planejamento(request):
    return HttpResponse ('<h1> teste </h1>')

def movimentacoes(request):
    return HttpResponse ('<h1> teste </h1>')

def settings(request):
    return none

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro\cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse(status=409)
        
        return HttpResponse(username)


def login(request):
    return render(request, 'login\login.html')