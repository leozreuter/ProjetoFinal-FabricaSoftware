from django.db import models
from django.contrib.auth.models import User

class Planejamento(models.Model): #Depois de fazer o model tem que realizar a migration: python manage.py makemigrations / python manage.py migrate
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    objetivo = models.DecimalField(max_digits=10, decimal_places=2)
    investimento_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    saldo_atual = models.DecimalField(max_digits=10, decimal_places=2, default=200.00)
    concluido = models.BooleanField(default=False)

    @property
    def barra(self):
        barra = int((self.saldo_atual * 100) // self.objetivo)
        if barra >= 100:
            barra = 100
            concluido = True
        
        return barra

    def __str__(self):
        return self.titulo