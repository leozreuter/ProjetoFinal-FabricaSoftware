from django.test import TestCase
from django.contrib.auth.models import User
from .models import Planejamento
from .planejamentos import Planejamentos
from datetime import timedelta
from django.utils import timezone

class PlanejamentosTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.planejamento = Planejamento.objects.create(
            titulo="Teste",
            objetivo=1000,
            investimento_mensal=100,
            data=timezone.now().date() - timedelta(days=30),
            usuario=self.user,
            saldo_atual=0
        )

    def test_atualizar_investimentos_mensais(self):
        planejamentos = Planejamentos(self.user)
        planejamentos.atualizar_investimentos_mensais()
        self.planejamento.refresh_from_db()
        self.assertEqual(self.planejamento.saldo_atual, 100)