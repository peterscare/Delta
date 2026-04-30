# components/home.py

"""
Tela principal do Delta.

Responsável por:
- exibir dados do usuário;
- mostrar saldo de Deltas;
- mostrar progresso;
- recomendar Learn Reel;
- mostrar missão do dia;
- destacar recompensa;
- mostrar Top 3 do ranking.
"""

import random
import streamlit as st

from data.learn_reels import recomendar_learn_reels
from data.recompensas import obter_recompensa_em_destaque


RANKING_BASE = [
    {
        "nome_publico": "Relâmpago McQueen",
        "curso": "Engenharia Mecânica",
        "deltas": 1250,
    },
    {
        "nome_publico": "Ana Clara",
        "curso": "Engenharia Civil",
        "deltas": 1180,
    },
    {
        "nome_publico": "Naruto",
        "curso": "Ciência da Computação",
        "deltas": 1100,
    },
    {
        "nome_publico": "Bob Esponja",
        "curso": "Engenharia de Produção",
        "deltas": 980,
    },
    {
        "nome_publico": "Homem-Aranha",
        "curso": "Engenharia Civil",
        "deltas": 900,
    },
]


def gerar_ranking_home(usuario):
    """
    Gera ranking simples para exibição na Home.
    """

    ranking = RANKING_BASE.copy()

    if usuario.get("aparecer_ranking"):
        ranking.append(
            {
                "nome_publico": usuario.get("nome_publico", "Aluno Delta"),
                "curso": usuario.get("curso", "Curso não informado"),
                "deltas": st.session_state.get("deltas", 0),
            }
        )

    ranking = sorted(
        ranking,
        key=lambda aluno: aluno["deltas"],
        reverse=True
    )

    return ranking


def exibir_home():
    """
    Exibe a tela principal do aplicativo.
    """

    usuario = st.session_state.usuario

    st.title("Δ Delta")
    st.subheader(f"Olá, {usuario['nome']}!")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Curso", usuario["curso"])
    col2.metric("Período", usuario["periodo"])
    col3.metric("Saldo", f"{st.session_state.deltas} Deltas")
    col4.metric("Progresso", f"{st.session_state.progresso}%")

    st.divider()

    st.markdown("## Missão do dia")
    st.info(
        "Assista 1 Learn Reel e responda 1 exercício para ganhar Deltas "
        "e subir no ranking."
    )

    st.divider()

    st.markdown("## Recomendado para você")

    reels_recomendados = recomendar_learn_reels(
        usuario["curso"],
        usuario["interesses"],
        limite=5
    )

    if reels_recomendados:
        reel = random.choice(reels_recomendados)

        with st.container(border=True):
            st.markdown(f"### {reel['titulo']}")
            st.caption(f"Tema: {reel['tema_calculo']} | Curso: {reel['curso']}")
            st.write(reel["descricao"])
            st.write(f"Duração estimada: **{reel['duracao_segundos']} segundos**")
            st.write(f"Recompensa: **{reel['recompensa_deltas']} Deltas**")

    else:
        st.warning("Nenhum Learn Reel recomendado no momento.")

    st.divider()

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("## Recompensa em destaque")

        recompensa = obter_recompensa_em_destaque(st.session_state.deltas)

        if recompensa:
            with st.container(border=True):
                st.markdown(f"### {recompensa['nome']}")
                st.write(recompensa["descricao"])
                st.write(f"Custo: **{recompensa['custo_deltas']} Deltas**")
                st.caption(f"Parceiro: {recompensa['parceiro']}")
        else:
            st.warning("Nenhuma recompensa disponível.")

    with col_b:
        st.markdown("## Top 3 Ranking Geral")

        ranking = gerar_ranking_home(usuario)[:3]

        for posicao, aluno in enumerate(ranking, start=1):
            st.write(
                f"**{posicao}º** {aluno['nome_publico']} — "
                f"{aluno['curso']} — **{aluno['deltas']} Deltas**"
            )