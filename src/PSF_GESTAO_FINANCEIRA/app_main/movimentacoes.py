from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from .models import Movimentacoes, PerfilUsuario
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from django.db.models import Sum

class MovimentacoesManutencao:

    def __init__(self, user):
        self.user = user

    def calcular_saldo(self):
        movimentacoes_usuario = Movimentacoes.objects.filter(usuario=self.user)
        saldo_atual = Decimal('0.00')  #Inicializa saldo_atual como Decimal
        ganhos_totais = Decimal('0.00')  #Inicializa saldo_atual como Decimal
        despesa_total = Decimal('0.00')  #Inicializa saldo_atual como Decimal
        for mov in movimentacoes_usuario:
            if mov.ganho:
                saldo_atual += mov.valor_movimentacao
                ganhos_totais = mov.valor_movimentacao + ganhos_totais
            else:
                saldo_atual -= mov.valor_movimentacao
                despesa_total = mov.valor_movimentacao + despesa_total

        return saldo_atual, ganhos_totais, despesa_total

    def atualizar_saldo_usuario(self):
        try:
            perfil_usuario, created = PerfilUsuario.objects.get_or_create(user=self.user)
            perfil_usuario.saldo_atual = self.calcular_saldo()
            
            #Calcula o valor total de ganhos e despesas separadamente
            ganhos = Movimentacoes.objects.filter(usuario=self.user, ganho=True).aggregate(total=Sum('valor_movimentacao'))['total'] or Decimal('0.00')
            despesas = Movimentacoes.objects.filter(usuario=self.user, ganho=False).aggregate(total=Sum('valor_movimentacao'))['total'] or Decimal('0.00')
            
            #Calcula o saldo total subtraindo as despesas dos ganhos
            saldo_total = ganhos - despesas
            
            perfil_usuario.valor_total_movimentacoes = saldo_total
            perfil_usuario.save()
        except Exception as e:
            print(f"Erro ao atualizar saldo do usuário: {e}")

    def criar_movimentacao(self, valor_movimentacao, descricao, ganho):
        try:
            nova_movimentacao = Movimentacoes(
                valor_movimentacao=valor_movimentacao,
                descricao=descricao,
                ganho=ganho,
                usuario=self.user,
            )
            nova_movimentacao.save()

            self.atualizar_saldo_usuario()
        except Exception as e:
            print(f"Erro ao criar movimentação: {e}")

    def editar_movimentacao():
        print("edita")

    def excluir_movimentacao(self, movimentacao_id):
        try:
            movimentacao = Movimentacoes.objects.get(id=movimentacao_id, usuario=self.user)
            movimentacao.delete()
            return True
        except Movimentacoes.DoesNotExist:
            return False

    def listar_movimentacoes(self):
        return Movimentacoes.objects.filter(usuario=self.user)