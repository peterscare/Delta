# src/services/progresso.py
"""
Métricas de progresso do aluno (para a Home e tela de perfil).
"""

from src.data.learn_reels import LEARN_REELS
from src.data.exercicios import EXERCICIOS


def estatisticas_usuario(usuario):
    total_reels = len(LEARN_REELS)
    total_exercicios = len(EXERCICIOS)

    reels_assistidos = len(usuario.reels_assistidos)
    exercicios_feitos = len(usuario.exercicios_concluidos)
    exercicios_acertados = len(usuario.exercicios_acertados)

    taxa_acerto = 0.0
    if exercicios_feitos > 0:
        taxa_acerto = exercicios_acertados / exercicios_feitos

    progresso_reels = reels_assistidos / total_reels if total_reels else 0
    progresso_exercicios = exercicios_feitos / total_exercicios if total_exercicios else 0

    return {
        "total_reels": total_reels,
        "reels_assistidos": reels_assistidos,
        "progresso_reels": progresso_reels,
        "total_exercicios": total_exercicios,
        "exercicios_feitos": exercicios_feitos,
        "exercicios_acertados": exercicios_acertados,
        "taxa_acerto": taxa_acerto,
        "progresso_exercicios": progresso_exercicios,
        "sequencia_dias": usuario.sequencia_dias,
        "deltas": usuario.deltas,
        "deltas_totais": usuario.deltas_totais,
    }
