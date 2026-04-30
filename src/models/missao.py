class Missao:
    def __init__(self, id, titulo, descricao, objetivo_contagem, premio_deltas, tema_calculo):
        """
        id: ID da missão.
        titulo: Nome da missão.
        descricao: O que o aluno deve fazer.
        objetivo_contagem: Quantos itens (vídeos/exercícios) completar.
        premio_deltas: Valor em Deltas ao concluir.
        tema_calculo: Tópico da ementa UFRJ relacionado.
        """
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.objetivo_contagem = objetivo_contagem
        self.premio_deltas = premio_deltas
        self.tema_calculo = tema_calculo
        self.concluida = False
from src.models.missao import Missao

# Missões baseadas na ementa de Cálculo I da UFRJ[cite: 1]
LISTA_MISSOES = [
    # Bloco 1: Limites e Continuidade
    Missao(
        id=1,
        titulo="O mestre do Limite",
        descricao="Assista a 3 Learn Reels sobre Limites Laterais e Infinitos.",
        objetivo_contagem=3,
        premio_deltas=50,
        tema_calculo="Limites e Continuidade"
    ),
    
    # Bloco 2: Derivadas
    Missao(
        id=2,
        titulo="Derivada Relâmpago",
        descricao="Acerte 5 exercícios de Regra da Cadeia seguidos.",
        objetivo_contagem=5,
        premio_deltas=100,
        tema_calculo="Derivadas"
    ),
    
    # Bloco 3: Aplicações de Derivada
    Missao(
        id=3,
        titulo="Engenheiro Otimizador",
        descricao="Conclua o desafio de problemas de Máximos e Mínimos aplicados ao seu curso.",
        objetivo_contagem=1,
        premio_deltas=150,
        tema_calculo="Aplicações de Derivadas"
    ),
    
    # Bloco 4: Integrais
    Missao(
        id=4,
        titulo="Explorador de Áreas",
        descricao="Assista ao vídeo introdutório sobre o Teorema Fundamental do Cálculo.",
        objetivo_contagem=1,
        premio_deltas=80,
        tema_calculo="Integrais"
    ),
    
    # Missão de Constância (Foco do Projeto Delta)[cite: 1]
    Missao(
        id=5,
        titulo="Semana de Ferro na UFRJ",
        descricao="Mantenha uma sequência de estudos de 5 dias seguidos no app.",
        objetivo_contagem=5,
        premio_deltas=300,
        tema_calculo="Geral"
    )
]

def obter_missoes_ativas():
    return LISTA_MISSOES