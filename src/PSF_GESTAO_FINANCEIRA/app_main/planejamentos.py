from .models import Planejamento

class Planejamentos:
    
    def __init__(self, user):
        self.user = user

    def criar_planejamento(self, form):
        if form.is_valid():
            planejamento = form.save(commit=False)
            planejamento.usuario = self.user
            planejamento.save()
            return True
        return False

    def listar_planejamentos(self):
        return Planejamento.objects.filter(usuario=self.user)

    def editar_planejamento(self, planejamento_id, form):
        planejamento = Planejamento.objects.get(id=planejamento_id, usuario=self.user)
        if form.is_valid():
            form.save()
            return True
        return False