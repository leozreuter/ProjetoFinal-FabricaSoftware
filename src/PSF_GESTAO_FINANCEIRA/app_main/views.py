from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home\home.html')

def planejamento(request):
    return HttpResponse ('<h1> teste </h1>')

def movimentacoes(request):
    return HttpResponse ('<h1> teste </h1>')

def settings(request):
    return none