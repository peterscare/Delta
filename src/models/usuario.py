class Usuario:
    def __init__(self, nome, curso, interesses=None):
        self.nome = nome
        self.curso = curso  # Engenharia Civil, Mecânica, Computação, etc.
        self.interesses = interesses if interesses else []
        self.deltas = 0  # Moeda interna do app
        self.sequencia_dias = 0  # Para gamificação de constância
        self.reels_assistidos = []
        self.exercicios_concluidos = []

    def adicionar_deltas(self, quantidade):
        self.deltas += quantidade