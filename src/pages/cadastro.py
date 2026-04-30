# src/pages/cadastro.py
"""Tela de boas-vindas / cadastro inicial — estilo onboarding de app moderno."""

import streamlit as st
from src.models.usuario import Usuario
from src.data.cursos import listar_nomes_cursos
from src.data.interesses import listar_interesses
from src.utils.session_state import logar


def render():
    st.markdown(
        """
        <div class="delta-login-hero">
            <div class="delta-bigΔ">Δ</div>
            <h1>Delta</h1>
            <p>Estude Cálculo, acumule <b>Deltas</b><br>e troque por vantagens reais.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="delta-login-features">
            <div class="delta-login-feature">
                <div class="delta-login-feature-icon">🎬</div>
                <div class="delta-login-feature-title">Learn Reels</div>
                <div class="delta-login-feature-desc">Cálculo em vídeos curtos</div>
            </div>
            <div class="delta-login-feature">
                <div class="delta-login-feature-icon">🎯</div>
                <div class="delta-login-feature-title">Personalizado</div>
                <div class="delta-login-feature-desc">Conteúdo do seu curso</div>
            </div>
            <div class="delta-login-feature">
                <div class="delta-login-feature-icon">🏆</div>
                <div class="delta-login-feature-title">Recompensas</div>
                <div class="delta-login-feature-desc">Vantagens reais na UFRJ</div>
            </div>
            <div class="delta-login-feature">
                <div class="delta-login-feature-icon">🔥</div>
                <div class="delta-login-feature-title">Ofensiva</div>
                <div class="delta-login-feature-desc">Estude todo dia</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Vamos te conhecer")

    with st.form("cadastro_inicial", clear_on_submit=False):
        nome = st.text_input("Como podemos te chamar?", placeholder="Seu nome ou apelido")

        curso = st.selectbox(
            "Qual seu curso na UFRJ?",
            listar_nomes_cursos(),
            index=0,
        )

        interesses = st.multiselect(
            "O que mais te interessa? (escolha 2 ou mais)",
            listar_interesses(),
            default=[],
            help="Vamos usar isso pra personalizar seus Learn Reels e exercícios.",
        )

        submitted = st.form_submit_button("Entrar no Delta 🚀", type="primary", use_container_width=True)

        if submitted:
            if not nome.strip():
                st.warning("Conta pra gente como te chamar 😉")
            else:
                novo = Usuario(nome=nome.strip(), curso=curso, interesses=interesses)
                # Bônus de boas-vindas
                novo.adicionar_deltas(20)
                logar(novo)
                st.rerun()
