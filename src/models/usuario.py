# src/models/usuario.py
"""
Modelo de Usuário do Delta.

Guarda os dados do aluno em sessão: identificação, curso, interesses,
saldo de Deltas, sequência de estudos e histórico de atividades.
"""

from datetime import date


class Usuario:
    def __init__(self, nome, curso, interesses=None):
        self.nome = nome
        self.curso = curso
        self.interesses = list(interesses) if interesses else []

        # Economia interna
        self.deltas = 0  # saldo atual
        self.deltas_totais = 0  # histórico (não diminui com resgates)

        # Gamificação
        self.sequencia_dias = 1
        self.ultimo_acesso = date.today()

        # Histórico
        self.reels_assistidos = []        # IDs
        self.exercicios_concluidos = []   # IDs
        self.exercicios_acertados = []    # IDs
        self.recompensas_resgatadas = []  # lista de dicts
        self.missoes_concluidas = []      # IDs

    # ----- saldo -----
    def adicionar_deltas(self, quantidade):
        if quantidade <= 0:
            return
        self.deltas += quantidade
        self.deltas_totais += quantidade

    def gastar_deltas(self, quantidade):
        if quantidade < 0:
            return False
        if self.deltas < quantidade:
            return False
        self.deltas -= quantidade
        return True

    # ----- atividades -----
    def registrar_reel(self, reel_id, recompensa=0):
        if reel_id not in self.reels_assistidos:
            self.reels_assistidos.append(reel_id)
            self.adicionar_deltas(recompensa)
            return True
        return False

    def registrar_exercicio(self, exercicio_id, acertou, recompensa=0):
        if exercicio_id not in self.exercicios_concluidos:
            self.exercicios_concluidos.append(exercicio_id)
        if acertou and exercicio_id not in self.exercicios_acertados:
            self.exercicios_acertados.append(exercicio_id)
            self.adicionar_deltas(recompensa)

    # ----- sequência -----
    def atualizar_sequencia(self):
        hoje = date.today()
        diff = (hoje - self.ultimo_acesso).days
        if diff == 0:
            pass  # já contou hoje
        elif diff == 1:
            self.sequencia_dias += 1
        else:
            self.sequencia_dias = 1
        self.ultimo_acesso = hoje
