from django.db import models
from django.contrib.auth.models import User

class Planejamento(models.Model): #Depois de fazer o model tem que realizar a migration: python manage.py makemigrations / python manage.py migrate
    """
    Representa um planejamento financeiro do usuário.

    Atributos:
        usuario (User): Referência ao usuário que criou o planejamento.
        titulo (str): Título do planejamento.
        objetivo (Decimal): Valor objetivo a ser alcançado pelo planejamento.
        investimento_mensal (Decimal): Valor mensal investido no planejamento.
        data (date): Data do planejamento.
        saldo_atual (Decimal): Saldo atual do planejamento.
        concluido (bool): Indica se o planejamento foi concluído.

    Métodos:
        barra(): Calcula a porcentagem do objetivo alcançado.
        concluidoSet(): Getter e setter para o atributo concluido.
        __str__(): Retorna uma representação em string do planejamento.
    """

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    objetivo = models.DecimalField(max_digits=10, decimal_places=2)
    investimento_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    saldo_atual = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    concluido = models.BooleanField(default=False)
    

    @property
    def barra(self):
        """
        Calcula a porcentagem do objetivo alcançado.

        Returns:
            int: Porcentagem do objetivo alcançado, variando de 0 a 100.
        """
        barra = int((self.saldo_atual * 100) // self.objetivo)
        if barra >= 100:
            barra = 100
            self.concluidoSet = True

        return barra
    
    @property
    def concluidoSet(self):
        return self.concluido
    
    @concluidoSet.setter
    def concluidoSet(self, valor):
        self.concluido = valor

    def __str__(self):
        return self.titulo
    
class Movimentacoes(models.Model):
    """
    Representa as movimentações financeiras associadas a um planejamento.

    Atributos:
        usuario (User): Referência ao usuário que criou a movimentação.
        valor_movimentacao (Decimal): Valor da movimentação financeira.
        descricao (str): Descrição da movimentação.
        ganho (bool): Indica se a movimentação é um ganho (True) ou uma despesa (False).
        data_criacao(Date): indica a data que foi inserida a movimentação
    """
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor_movimentacao = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200)
    ganho = models.BooleanField(default=False)
    data_criacao = models.DateField(auto_now_add=True)

class PerfilUsuario(models.Model):
    """
    Tabela para vincular o valor total das movimentações com o usuario

    Atributos:
        usuario (User): Referência ao usuário.
        valor_total_movimentacoes(Decimal): valor total das movimentações(Gastos e Despesas)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    valor_total_movimentacoes = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
