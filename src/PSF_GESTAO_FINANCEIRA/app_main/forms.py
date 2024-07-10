from django import forms
from .models import Planejamento

class PlanejamentoForm(forms.ModelForm):
    """
    Formulário para criação e edição de Planejamentos.

    Este formulário utiliza a model Planejamento e inclui os campos:
    - titulo
    - objetivo
    - investimento_mensal
    - data
    - saldo_atual

    Os formulários em Django servem para facilitar o envio de dados dos formulários HTML
    para as models, garantindo que os dados sejam validados e salvos corretamente no banco de dados.
    """

    class Meta:
        model = Planejamento  #Define que este formulário está vinculado ao modelo Planejamento
        fields = ['titulo','objetivo', 'investimento_mensal', 'data', 'saldo_atual']
