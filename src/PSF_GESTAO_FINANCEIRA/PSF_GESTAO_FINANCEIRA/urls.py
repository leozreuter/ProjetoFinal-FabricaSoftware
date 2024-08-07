"""
URL configuration for PSF_GESTAO_FINANCEIRA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from app_main import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('planejamentos/', views.planejamentos , name='planejamentos'),
    path('movimentacoes/', views.movimentacoes , name='movimentacoes'),
    path('configuracoes/', views.configuracoes , name='configuracoes'),
    path('perfil/', views.perfil , name='perfil'),
    path('logout/', views.logout_view , name='logout'),
    path('edit-planejamento/<int:planejamento_id>/', views.editplanej , name='editplanej'),  
    path('newplanejamento/', views.newplanejamento , name='newplanejamento'),
    path('confirmar-exclusão/<int:planejamento_id>/', views.excluirplanej, name='deleteplanejamento'),
    path('newmovimentacao/', views.newmovimentacao, name='newmovimentacao'),

    # QUALQUER URL QUE NÃO EXISTA REDIRECIONA PARA A HOME
    path('<path:qualquer_caminho>', RedirectView.as_view(url='/'))
]
