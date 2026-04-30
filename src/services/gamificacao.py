# src/services/gamificacao.py
"""
Regras de gamificação do Delta.

Centraliza:
- bônus de sequência (streak)
- avaliação de progresso de missões
- atualização do nível do aluno
"""

from src.data.missoes import listar_missoes


def bonus_sequencia(sequencia_dias):
    """
    Retorna Deltas extras por manter sequência diária.
    """
    if sequencia_dias >= 7:
        return 50
    if sequencia_dias >= 3:
        return 20
    if sequencia_dias >= 2:
        return 5
    return 0


def calcular_nivel(deltas_totais):
    """
    Sistema de níveis baseado em Deltas acumulados (histórico).
    """
    if deltas_totais >= 1000:
        return ("Mestre Delta", "🌟")
    if deltas_totais >= 500:
        return ("Avançado", "🚀")
    if deltas_totais >= 200:
        return ("Intermediário", "💪")
    if deltas_totais >= 50:
        return ("Iniciante", "🌱")
    return ("Calouro", "🐣")


def avaliar_missoes(usuario):
    """
    Atualiza progresso das missões com base nas atividades do usuário.
    Retorna lista de missões recém-concluídas (e seus prêmios) para o
    front-end exibir conquistas.
    """
    recém_concluidas = []
    for missao in listar_missoes():
        if missao.id in usuario.missoes_concluidas:
            continue

        progresso = 0
        if missao.tema_calculo == "Geral":
            progresso = usuario.sequencia_dias
        elif missao.tema_calculo == "Limites e Continuidade":
            # contar reels assistidos com tema Limites/Continuidade
            from src.data.learn_reels import buscar_learn_reel_por_id
            for rid in usuario.reels_assistidos:
                reel = buscar_learn_reel_por_id(rid)
                if reel and reel["tema_calculo"] in ("Limites", "Continuidade"):
                    progresso += 1
        elif missao.tema_calculo == "Derivadas":
            from src.data.exercicios import buscar_exercicio_por_id
            for eid in usuario.exercicios_acertados:
                ex = buscar_exercicio_por_id(eid)
                if ex and ex["tema_calculo"] == "Derivadas":
                    progresso += 1
        elif missao.tema_calculo == "Integrais":
            from src.data.learn_reels import buscar_learn_reel_por_id
            for rid in usuario.reels_assistidos:
                reel = buscar_learn_reel_por_id(rid)
                if reel and reel["tema_calculo"] == "Integrais":
                    progresso += 1
        elif missao.tema_calculo == "Aplicações de Derivadas":
            from src.data.exercicios import buscar_exercicio_por_id
            for eid in usuario.exercicios_acertados:
                ex = buscar_exercicio_por_id(eid)
                if ex and ex["tema_calculo"] == "Otimização":
                    progresso += 1

        missao.progresso_atual = progresso

        if progresso >= missao.objetivo_contagem and not missao.concluida:
            missao.concluida = True
            usuario.missoes_concluidas.append(missao.id)
            usuario.adicionar_deltas(missao.premio_deltas)
            recém_concluidas.append(missao)

    return recém_concluidas
