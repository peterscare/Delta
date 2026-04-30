class Exercicio:
    def __init__(self, id, curso_alvo, tema, enunciado, opcoes, correta, recompensa_deltas):
        self.id = id
        self.curso_alvo = curso_alvo  # Ex: 'Engenharia Civil'
        self.tema = tema  # Ex: 'Derivadas'
        self.enunciado = enunciado
        self.opcoes = opcoes  # Lista de 4 opções
        self.correta = correta
        self.recompensa_deltas = recompensa_deltas  # Valor ganho ao acertar[cite: 1]