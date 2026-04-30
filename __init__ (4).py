# src/services/personalizacao.py
"""
Regras de personalização do Delta.

Combina curso + interesses do aluno para retornar Learn Reels e
exercícios sob medida.
"""

from src.data.learn_reels import recomendar_learn_reels
from src.data.exercicios import recomendar_exercicios
from src.data.cursos import obter_temas_por_curso


def feed_personalizado(usuario, limite=10):
    """Retorna Learn Reels sugeridos para o usuário."""
    return recomendar_learn_reels(usuario.curso, usuario.interesses, limite=limite)


def exercicios_personalizados(usuario, limite=10):
    """Retorna exercícios sugeridos para o usuário."""
    return recomendar_exercicios(usuario.curso, usuario.interesses, limite=limite)


def temas_relevantes(usuario):
    """Temas de Cálculo I que mais dialogam com o curso do aluno."""
    return obter_temas_por_curso(usuario.curso)
