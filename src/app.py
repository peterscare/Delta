# src/app.py
"""
Delta — Projeto Hackathon UFRJ.

Plataforma gamificada de apoio ao estudo de Cálculo I.
"""

import os
import streamlit as st

from src.utils.session_state import (
    inicializar_estado,
    usuario_atual,
    ir_para,
)

from src.pages import (
    cadastro,
    home,
    learn_reels_page,
    exercicios_page,
    loja,
    ranking_page,
    sobre,
)


# ============ CONFIG ============
st.set_page_config(
    page_title="Delta — UFRJ",
    page_icon="Δ",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ============ CSS ============
def carregar_css():
    css_path = os.path.join(os.path.dirname(__file__), "styles", "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ============ NAVBAR ============
def render_navbar():
    """Barra de navegação inferior estilo app."""
    user = usuario_atual()
    if user is None:
        return

    pagina_atual = st.session_state.get("pagina", "Home")

    # Renderizada como botões em colunas
    st.markdown("---")
    col1, col2, col3, col4, col5 = st.columns(5)

    botoes = [
        (col1, "🏠", "Home"),
        (col2, "🎬", "Learn Reels"),
        (col3, "✏️", "Exercícios"),
        (col4, "🏆", "Ranking"),
        (col5, "👤", "Perfil"),
    ]

    for col, icone, pagina in botoes:
        with col:
            ativo = pagina_atual == pagina or (pagina == "Perfil" and pagina_atual == "Sobre")
            label = f"{icone}\n{pagina if pagina != 'Learn Reels' else 'Reels'}"
            if st.button(label, key=f"nav_{pagina}", use_container_width=True, type="primary" if ativo else "secondary"):
                # Loja é acessada via Home/botão dedicado, mas mantemos rota:
                ir_para(pagina if pagina != "Perfil" else "Sobre")
                st.rerun()


# ============ ROUTER ============
def router():
    pagina = st.session_state.get("pagina", "Home")
    if pagina == "Home":
        home.render()
    elif pagina == "Learn Reels":
        learn_reels_page.render()
    elif pagina == "Exercícios":
        exercicios_page.render()
    elif pagina == "Loja":
        loja.render()
    elif pagina == "Ranking":
        ranking_page.render()
    elif pagina == "Sobre":
        sobre.render()
    else:
        home.render()


# ============ MAIN ============
def main():
    carregar_css()
    inicializar_estado()

    user = usuario_atual()
    if user is None:
        cadastro.render()
        return

    router()
    render_navbar()


if __name__ == "__main__":
    main()
