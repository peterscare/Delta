# src/models/recompensa.py


class Recompensa:
    """Representação OO de uma recompensa (os dados ficam em
    src/data/recompensas.py como dicts)."""

    def __init__(self, id, nome, descricao, custo_deltas, tipo,
                 parceiro="Projeto Delta", ativa=True, depende_validacao=False,
                 icone="🎁"):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.custo_deltas = custo_deltas
        self.tipo = tipo
        self.parceiro = parceiro
        self.ativa = ativa
        self.depende_validacao = depende_validacao
        self.icone = icone

    def pode_resgatar(self, saldo_usuario):
        return self.ativa and saldo_usuario >= self.custo_deltas
