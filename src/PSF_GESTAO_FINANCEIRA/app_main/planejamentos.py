from .models import Planejamento

class Planejamentos:
    """
    Classe que fornece métodos para manipulação de objetos Planejamento relacionados a um usuário específico.

    Atributos:
        user (User): Usuário para o qual os planejamentos são manipulados.

    Métodos:
        __init__(user): Inicializa a classe com o usuário especificado.
        criar_planejamento(form): Cria um novo planejamento com base nos dados do formulário.
        listar_planejamentos(): Retorna todos os planejamentos do usuário.
        editar_planejamento(planejamento_id, form): Edita um planejamento existente com base nos dados do formulário.
        excluir_planejamento(planejamento_id): Exclui um planejamento existente com base no ID fornecido.
    """

    def __init__(self, user):
        """
        Inicializa a classe com o usuário especificado.

        Parametros:
            user (User): Usuário para o qual os planejamentos serão manipulados.
        """
        self.user = user

    def criar_planejamento(self, form):
        """
        Cria um novo planejamento com base nos dados do formulário.

        Parametros:
            form (PlanejamentoForm): Formulário contendo os dados do novo planejamento.

        Returns:
            bool: True se o planejamento foi criado com sucesso, False caso contrário.
        """
        if form.is_valid():
            planejamento = form.save(commit=False)
            planejamento.usuario = self.user
            planejamento.save()
            return True
        return False

    def listar_planejamentos(self):
        """
        Retorna todos os planejamentos do usuário.

        Returns:
            QuerySet: QuerySet contendo todos os planejamentos do usuário.
        """
        return Planejamento.objects.filter(usuario=self.user)

    def editar_planejamento(self, planejamento_id, form):
        """
        Edita um planejamento existente com base nos dados do formulário.

        Parametros:
            planejamento_id (int): ID do planejamento a ser editado.
            form (PlanejamentoForm): Formulário contendo os dados atualizados do planejamento.

        Returns:
            bool: True se o planejamento foi editado com sucesso, False caso contrário.
        """
        try:
            planejamento = Planejamento.objects.get(id=planejamento_id, usuario=self.user)
            if form.is_valid():
                planejamento = form.save(commit=False)
                planejamento.usuario = self.user  # Certifique-se de que o usuário seja atribuído corretamente
                planejamento.save()
                return True
        except Planejamento.DoesNotExist:
            return False
    
    def excluir_planejamento(self, planejamento_id):
        """
        Exclui um planejamento existente com base no ID fornecido.

        Parametros:
            planejamento_id (int): ID do planejamento a ser excluído.

        Returns:
            bool: True se o planejamento foi excluído com sucesso, False caso contrário.
        """
        try:
            planejamento = Planejamento.objects.get(id=planejamento_id, usuario=self.user)
            planejamento.delete()
            return True
        except Planejamento.DoesNotExist:
            return False
