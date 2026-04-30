# src/pages/exercicios_page.py
"""Exercícios rápidos — estilo quiz com feedback imediato."""

import streamlit as st

from src.utils.session_state import usuario_atual
from src.utils.helpers import emoji_tema, formatar_deltas
from src.services.personalizacao import exercicios_personalizados


def render():
    user = usuario_atual()
    if user is None:
        return

    st.markdown(
        f"""
        <div class="delta-header">
            <div class="delta-logo">Praticar</div>
            <div class="delta-balance">⚡ {formatar_deltas(user.deltas)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    exs = exercicios_personalizados(user, limite=15)
    if not exs:
        st.info("Sem exercícios disponíveis.")
        return

    if "exercicio_index" not in st.session_state:
        st.session_state.exercicio_index = 0
    if st.session_state.exercicio_index >= len(exs):
        st.session_state.exercicio_index = 0

    ex = exs[st.session_state.exercicio_index]
    fb_key = f"feedback_ex_{ex['id']}"

    # Stats no topo
    col1, col2, col3 = st.columns(3)
    col1.metric("Exercício", f"{st.session_state.exercicio_index + 1}/{len(exs)}")
    col2.metric("Acertos", len(user.exercicios_acertados))
    col3.metric("Sequência", f"🔥 {user.sequencia_dias}d")

    # Card do exercício
    st.markdown(
        f"""
        <div class="delta-exercise-card">
            <div class="delta-exercise-meta">
                <span class="delta-tag">{emoji_tema(ex['tema_calculo'])} {ex['tema_calculo']}</span>
                <span class="delta-tag">📊 {ex['dificuldade']}</span>
                <span class="delta-tag">+{ex['recompensa_deltas']} Δ</span>
            </div>
            <div class="delta-exercise-question">{ex['pergunta']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Alternativas via radio
    feedback = st.session_state.get(fb_key)
    desabilitar = feedback is not None

    resposta = st.radio(
        "Sua resposta:",
        ex["alternativas"],
        index=None,
        key=f"radio_ex_{ex['id']}_{st.session_state.exercicio_index}",
        disabled=desabilitar,
        label_visibility="collapsed",
    )

    col_check, col_skip = st.columns([2, 1])

    with col_check:
        if st.button("Confirmar resposta", type="primary", use_container_width=True, disabled=desabilitar or resposta is None):
            acertou = resposta == ex["resposta_correta"]
            recompensa = ex["recompensa_deltas"] if acertou else 0
            user.registrar_exercicio(ex["id"], acertou, recompensa)
            st.session_state[fb_key] = {
                "acertou": acertou,
                "resposta": resposta,
                "correta": ex["resposta_correta"],
                "explicacao": ex.get("explicacao", ""),
                "recompensa": recompensa,
            }
            if acertou:
                st.toast(f"+{recompensa} Deltas! 🎉", icon="✅")
            st.rerun()

    with col_skip:
        if st.button("Pular ➡️", use_container_width=True):
            # limpar feedback dessa questão
            if fb_key in st.session_state:
                del st.session_state[fb_key]
            st.session_state.exercicio_index = (st.session_state.exercicio_index + 1) % len(exs)
            st.rerun()

    # Feedback
    if feedback:
        if feedback["acertou"]:
            st.markdown(
                f"""
                <div class="delta-feedback-correto">
                    ✅ <b>Correto!</b> Você ganhou <b>+{feedback['recompensa']} Deltas</b>.<br>
                    <span style="font-size:13px;opacity:0.95;font-weight:400;">{feedback['explicacao']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="delta-feedback-errado">
                    ❌ <b>Não foi dessa vez.</b><br>
                    <span style="font-size:13px;opacity:0.95;font-weight:400;">
                        Resposta correta: <b>{feedback['correta']}</b><br>{feedback['explicacao']}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        if st.button("Próximo exercício →", use_container_width=True, type="primary"):
            del st.session_state[fb_key]
            st.session_state.exercicio_index = (st.session_state.exercicio_index + 1) % len(exs)
            st.rerun()
