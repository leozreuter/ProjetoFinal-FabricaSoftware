from django import forms
from .models import Planejamento

class PlanejamentoForm(forms.ModelForm):
    class Meta:
        model = Planejamento
        fields = ['titulo', 'objetivo', 'investimento_mensal', 'data']

#Os forms servem pra facilitar o envio de formulários mais facil para as models