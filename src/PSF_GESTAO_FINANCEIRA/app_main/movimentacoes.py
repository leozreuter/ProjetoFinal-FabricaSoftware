from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from .models import Movimentacoes, PerfilUsuario
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from django.db.models import Sum

class MovimentacoesManutencao:
    """
    Classe para gerenciar as movimentações
    """

    def __init__(self, user):
        #Inicializa o usuário
        self.user = user

    def calcular_saldo(self):

        """
        Calcula o saldo atual, ganhos totais e despesas totais do usuário.

        Returns:
            tuple: Uma tupla contendo o saldo atual (Decimal), ganhos totais (Decimal) e despesas totais (Decimal).
        """

        movimentacoes_usuario = Movimentacoes.objects.filter(usuario=self.user) #Filtra as movimentações pelo usuário que manda a requisição
        saldo_atual = Decimal('0.00')  #Inicializa saldo_atual como Decimal
        ganhos_totais = Decimal('0.00')  #Inicializa saldo_atual como Decimal
        despesa_total = Decimal('0.00')  #Inicializa saldo_atual como Decimal
        for mov in movimentacoes_usuario:
            if mov.ganho: #Verifica se é um ganho (TRUE), se não (FALSE)
                saldo_atual += mov.valor_movimentacao
                ganhos_totais = mov.valor_movimentacao + ganhos_totais
            else:
                saldo_atual -= mov.valor_movimentacao
                despesa_total = mov.valor_movimentacao + despesa_total

        return saldo_atual, ganhos_totais, despesa_total

    def atualizar_saldo_usuario(self):
        """
        Atualiza o saldo atual e o valor total de movimentações na tabela do perfil do usuário.
        """
        perfil_usuario, created = PerfilUsuario.objects.get_or_create(user=self.user) #verifica se o objeto ja foi criado no banco de dados, se o objeto ja existir created é FALSE se não é TRUE
        perfil_usuario.saldo_atual = self.calcular_saldo() #Salva no campo saldo_atual o saldo calculado
            
        #Calcula o valor total de ganhos e despesas separadamente
        ganhos = Movimentacoes.objects.filter(usuario=self.user, ganho=True).aggregate(total=Sum('valor_movimentacao'))['total'] or Decimal('0.00')
        despesas = Movimentacoes.objects.filter(usuario=self.user, ganho=False).aggregate(total=Sum('valor_movimentacao'))['total'] or Decimal('0.00')
            
        #Calcula o saldo total subtraindo as despesas dos ganhos
        saldo_total = ganhos - despesas
            
        perfil_usuario.valor_total_movimentacoes = saldo_total #Salva o saldo total na coluna valor_total_movimentacoes
        perfil_usuario.save() #E salva esse valor na tabela

    def criar_movimentacao(self, valor_movimentacao, descricao, ganho):
        """
        Cria uma nova movimentação e atualiza o saldo do usuário.

        Parâmetros:
            valor_movimentacao (Decimal): O valor da movimentação.
            descricao (str): A descrição da movimentação.
            ganho (bool): Indica se a movimentação é um ganho (True) ou uma despesa (False).
        """
        nova_movimentacao = Movimentacoes(
            valor_movimentacao=valor_movimentacao,
            descricao=descricao,
            ganho=ganho,
            usuario=self.user,
        )
        nova_movimentacao.save()

        self.atualizar_saldo_usuario() #Chama a função pra atuaizar o saldo na tabela

    def listar_movimentacoes(self):
        """
        Função pra listar todas as movimentações com base no usuário que está relacionado
        """
        return Movimentacoes.objects.filter(usuario=self.user)