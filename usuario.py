# src/models/exercicio.py


class Exercicio:
    """Representação OO de um exercício (opcional — os dados ficam em
    src/data/exercicios.py como dicts)."""

    def __init__(self, id, pergunta, alternativas, resposta_correta,
                 curso, tema_calculo, dificuldade, recompensa_deltas,
                 explicacao="", interesses=None):
        self.id = id
        self.pergunta = pergunta
        self.alternativas = alternativas
        self.resposta_correta = resposta_correta
        self.curso = curso
        self.tema_calculo = tema_calculo
        self.dificuldade = dificuldade
        self.recompensa_deltas = recompensa_deltas
        self.explicacao = explicacao
        self.interesses = interesses or []

    def verificar(self, resposta):
        return resposta == self.resposta_correta
