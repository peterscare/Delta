# src/services/ranking.py
"""
Ranking do Delta.

Combina o usuário atual com a base fictícia de outros estudantes para
gerar um ranking ordenado (e a posição do aluno).
"""

from src.data.ranking_base import obter_ranking_base


def gerar_ranking(usuario):
    """
    Retorna lista de dicts ordenada por Deltas (desc), incluindo o usuário.
    Cada item tem: nome, curso, deltas, eh_voce, posicao.
    """
    todos = obter_ranking_base()
    todos.append({
        "nome": usuario.nome,
        "curso": usuario.curso,
        "deltas": usuario.deltas_totais,
        "eh_voce": True,
    })

    for item in todos:
        item.setdefault("eh_voce", False)

    todos.sort(key=lambda x: x["deltas"], reverse=True)
    for posicao, item in enumerate(todos, start=1):
        item["posicao"] = posicao
    return todos


def posicao_do_usuario(usuario):
    ranking = gerar_ranking(usuario)
    for item in ranking:
        if item["eh_voce"]:
            return item["posicao"]
    return None


def ranking_por_curso(usuario):
    """Filtra o ranking apenas pelo curso do aluno."""
    return [r for r in gerar_ranking(usuario) if r["curso"] == usuario.curso]
