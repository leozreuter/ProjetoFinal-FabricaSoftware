from django.contrib.auth.models import User
from django.utils import timezone
from .models import Movimentacoes

class MovimentacoesManutencao:

    def __init__(self, user):
        self.user = user

    def criar_movimentacao(self, valor_movimentacao, descricao, ganho):
        nova_movimentacao = Movimentacoes(
            valor_movimentacao=valor_movimentacao,
            descricao=descricao,
            ganho=ganho,
            usuario=self.user, #Associando a movimentação ao usuário atual
        )
        nova_movimentacao.save()

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