from django.contrib.auth.models import User
from .models import Movimentacoes

class Movimentacoesm:

    def __init__(self, user):
        self.user = user

    def criar_movimentacao(self, valor_movimentacao, descricao, ganho):
        nova_movimentacao = Movimentacoes(
            valor_movimentacao=valor_movimentacao,
            descricao=descricao,
            ganho=ganho
        )
        nova_movimentacao.save()

    def editar_movimentacao():
        print("edita")

    def excluir_movimentacao():
        print("exclui")

    def listar_movimentacoes():
        print("lista")