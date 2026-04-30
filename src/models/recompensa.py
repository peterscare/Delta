class Recompensa:
    def __init__(self, id, nome, descricao, custo_deltas, tipo, estoque=None):
        """
        id: Identificador único da recompensa.
        nome: Nome atrativo (ex: 'Mentoria com Veterano').
        descricao: Explicação do benefício.
        custo_deltas: Valor necessário para o resgate.
        tipo: Categoria (ex: 'Institucional', 'Certificado', 'Cupom').
        estoque: Quantidade disponível (opcional).
        """
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.custo_deltas = custo_deltas
        self.tipo = tipo
        self.estoque = estoque

    def pode_resgatar(self, saldo_usuario):
        """Verifica se o aluno tem Deltas suficientes para a troca."""
        return saldo_usuario >= self.custo_deltas