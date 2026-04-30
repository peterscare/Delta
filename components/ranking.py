# components/ranking.py

"""
Tela de ranking do Delta.

Responsável por:
- exibir ranking geral;
- exibir ranking por curso;
- respeitar escolha do aluno sobre aparecer ou não no ranking.
"""

import streamlit as st


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
    {
        "nome_publico": "Sonic",
        "curso": "Engenharia Elétrica",
        "deltas": 850,
    },
    {
        "nome_publico": "Goku",
        "curso": "Física",
        "deltas": 790,
    },
]


def gerar_ranking(usuario):
    """
    Gera ranking com alunos fictícios e o aluno atual,
    caso ele tenha escolhido aparecer publicamente.
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


def exibir_ranking():
    """
    Exibe a tela de ranking.
    """

    usuario = st.session_state.usuario

    st.title("Ranking Delta")
    st.write(
        "Veja os alunos com maior pontuação. A identificação no ranking é opcional."
    )

    if not usuario.get("aparecer_ranking"):
        st.info(
            "Você escolheu não aparecer publicamente no ranking. "
            "Mesmo assim, pode visualizar a classificação dos outros alunos."
        )

    st.divider()

    filtro = st.radio(
        "Visualizar ranking",
        ["Geral", "Meu curso"],
        horizontal=True
    )

    ranking = gerar_ranking(usuario)

    if filtro == "Meu curso":
        ranking = [
            aluno
            for aluno in ranking
            if aluno["curso"] == usuario["curso"]
        ]

    if not ranking:
        st.warning("Nenhum aluno encontrado para este filtro.")
        return

    for posicao, aluno in enumerate(ranking, start=1):
        with st.container(border=True):
            col1, col2, col3 = st.columns([1, 3, 2])

            with col1:
                st.markdown(f"## {posicao}º")

            with col2:
                st.markdown(f"### {aluno['nome_publico']}")
                st.caption(aluno["curso"])

            with col3:
                st.metric("Deltas", aluno["deltas"])