# components/login.py

"""
Tela de login/cadastro do Delta.

Responsável por:
- coletar nome do aluno;
- coletar e-mail;
- selecionar curso;
- selecionar interesses;
- definir como o aluno aparecerá no ranking;
- registrar consentimento de personalização.
"""

import streamlit as st

from data.cursos import listar_nomes_cursos


INTERESSES = [
    "Tecnologia",
    "Esportes",
    "Jogos",
    "Música",
    "Cinema e séries",
    "Finanças",
    "Memes",
    "Empreendedorismo",
    "Ciência",
    "Cultura geek",
    "Desafios competitivos",
]


PERSONAGENS = [
    "Relâmpago McQueen",
    "Bob Esponja",
    "Homem-Aranha",
    "Naruto",
    "Sonic",
    "Shrek",
    "Dora Aventureira",
    "Perry, o Ornitorrinco",
    "Goku",
    "Finn, o Humano",
]


def exibir_login():
    """
    Exibe a tela inicial de cadastro/login.
    """

    st.title("Δ Delta")
    st.subheader("Cálculo I gamificado, personalizado e recompensador")

    st.write(
        "O Delta ajuda estudantes de Cálculo I a manter foco, constância e motivação "
        "por meio de Learn Reels, exercícios rápidos, Deltas, recompensas e ranking."
    )

    st.divider()

    with st.form("form_login"):
        st.markdown("### Cadastro inicial")

        nome = st.text_input("Nome")
        email = st.text_input("E-mail institucional")
        curso = st.selectbox("Curso", listar_nomes_cursos())
        periodo = st.selectbox(
            "Período",
            ["1º", "2º", "3º", "4º", "5º ou mais"]
        )

        interesses = st.multiselect(
            "Escolha seus interesses para personalizar a experiência",
            INTERESSES
        )

        st.markdown("### Ranking")

        aparecer_ranking = st.checkbox("Quero aparecer no ranking")

        tipo_identificacao = "Anônimo"
        nome_publico = "Anônimo"

        if aparecer_ranking:
            tipo_identificacao = st.radio(
                "Como deseja aparecer?",
                ["Nome real", "Apelido", "Nome de personagem"]
            )

            if tipo_identificacao == "Nome real":
                nome_publico = nome

            elif tipo_identificacao == "Apelido":
                nome_publico = st.text_input("Digite seu apelido")

            elif tipo_identificacao == "Nome de personagem":
                nome_publico = st.selectbox("Escolha um personagem", PERSONAGENS)

        consentiu_personalizacao = st.checkbox(
            "Aceito que o Delta use minhas preferências declaradas e meu uso dentro do app "
            "para personalizar recomendações."
        )

        enviar = st.form_submit_button("Entrar no Delta")

    if enviar:
        if not nome:
            st.error("Preencha seu nome para continuar.")
            return

        if not email:
            st.error("Preencha seu e-mail para continuar.")
            return

        if not interesses:
            st.error("Escolha pelo menos um interesse.")
            return

        if not consentiu_personalizacao:
            st.error("Para usar a personalização do Delta, é necessário aceitar o consentimento.")
            return

        if aparecer_ranking and not nome_publico:
            st.error("Escolha ou digite um nome público para o ranking.")
            return

        st.session_state.usuario = {
            "nome": nome,
            "email": email,
            "curso": curso,
            "periodo": periodo,
            "interesses": interesses,
            "aparecer_ranking": aparecer_ranking,
            "tipo_identificacao": tipo_identificacao,
            "nome_publico": nome_publico,
        }

        st.session_state.deltas = 50
        st.session_state.progresso = 0
        st.session_state.learn_reels_concluidos = []
        st.session_state.questoes_respondidas = []

        st.success("Cadastro realizado! Você ganhou 50 Deltas de boas-vindas.")
        st.rerun()