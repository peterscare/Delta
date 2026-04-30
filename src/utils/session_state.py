# src/utils/session_state.py
"""Helpers para inicializar e acessar o session_state do Streamlit."""

import streamlit as st


def inicializar_estado():
    """Garante que as chaves esperadas existam no session_state."""
    defaults = {
        "usuario": None,
        "pagina": "Home",
        "reel_index": 0,
        "exercicio_index": 0,
        "feedback_exercicio": None,
        "ultima_recompensa": None,
        "missoes_concluidas_recente": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def usuario_atual():
    return st.session_state.get("usuario")


def logar(usuario):
    st.session_state.usuario = usuario


def deslogar():
    st.session_state.usuario = None
    st.session_state.pagina = "Home"


def ir_para(pagina):
    st.session_state.pagina = pagina
