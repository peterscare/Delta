# src/models/missao.py
"""
Modelo de Missão do Delta.

Uma missão é um desafio curto (assistir N Learn Reels, acertar X
exercícios, manter sequência etc.) que recompensa o aluno em Deltas
ao ser concluído.
"""


class Missao:
    def __init__(self, id, titulo, descricao, objetivo_contagem, premio_deltas, tema_calculo):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.objetivo_contagem = objetivo_contagem
        self.premio_deltas = premio_deltas
        self.tema_calculo = tema_calculo
        self.concluida = False
        self.progresso_atual = 0  # quantos itens já cumpridos

    def progresso_percentual(self):
        if self.objetivo_contagem <= 0:
            return 0.0
        return min(self.progresso_atual / self.objetivo_contagem, 1.0)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "objetivo_contagem": self.objetivo_contagem,
            "premio_deltas": self.premio_deltas,
            "tema_calculo": self.tema_calculo,
            "concluida": self.concluida,
            "progresso_atual": self.progresso_atual,
        }
