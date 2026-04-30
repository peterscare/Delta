# src/data/missoes.py
"""
Missões do Delta — desafios curtos que dão Deltas extras
e direcionam o aluno pela ementa de Cálculo I da UFRJ.
"""

from src.models.missao import Missao


LISTA_MISSOES = [
    Missao(
        id=1,
        titulo="O mestre do Limite",
        descricao="Assista a 3 Learn Reels sobre Limites e Continuidade.",
        objetivo_contagem=3,
        premio_deltas=50,
        tema_calculo="Limites e Continuidade",
    ),
    Missao(
        id=2,
        titulo="Derivada Relâmpago",
        descricao="Acerte 5 exercícios de Derivadas seguidos.",
        objetivo_contagem=5,
        premio_deltas=100,
        tema_calculo="Derivadas",
    ),
    Missao(
        id=3,
        titulo="Engenheiro Otimizador",
        descricao="Conclua o desafio de Otimização aplicado ao seu curso.",
        objetivo_contagem=1,
        premio_deltas=150,
        tema_calculo="Aplicações de Derivadas",
    ),
    Missao(
        id=4,
        titulo="Explorador de Áreas",
        descricao="Assista ao Learn Reel introdutório sobre Integrais.",
        objetivo_contagem=1,
        premio_deltas=80,
        tema_calculo="Integrais",
    ),
    Missao(
        id=5,
        titulo="Semana de Ferro na UFRJ",
        descricao="Mantenha uma sequência de estudos de 5 dias seguidos no app.",
        objetivo_contagem=5,
        premio_deltas=300,
        tema_calculo="Geral",
    ),
]


def listar_missoes():
    return LISTA_MISSOES


# Alias usado em algumas partes do código
def obter_missoes_ativas():
    return LISTA_MISSOES


def buscar_missao_por_id(missao_id):
    for m in LISTA_MISSOES:
        if m.id == missao_id:
            return m
    return None
