# src/pages/ranking_page.py
"""Ranking — geral e por curso."""

import streamlit as st

from src.utils.session_state import usuario_atual
from src.utils.helpers import formatar_deltas, emoji_curso
from src.services.ranking import gerar_ranking, ranking_por_curso, posicao_do_usuario


def _avatar(nome):
    return "".join(p[0] for p in nome.split()[:2]).upper() or "?"


def _render_lista(ranking):
    medalhas = {1: "🥇", 2: "🥈", 3: "🥉"}
    html = ""
    for item in ranking[:30]:
        eh_voce = item.get("eh_voce", False)
        css = "delta-ranking-item eh-voce" if eh_voce else "delta-ranking-item"
        pos = item["posicao"]
        rotulo_pos = medalhas.get(pos, f"#{pos}")
        nome_label = f"{item['nome']} {'(você)' if eh_voce else ''}"
        html += f"""
            <div class="{css}">
                <div class="delta-ranking-position">{rotulo_pos}</div>
                <div class="delta-ranking-avatar">{_avatar(item['nome'])}</div>
                <div class="delta-ranking-info">
                    <div class="delta-ranking-name">{nome_label}</div>
                    <div class="delta-ranking-course">{emoji_curso(item['curso'])} {item['curso']}</div>
                </div>
                <div class="delta-ranking-deltas">⚡ {formatar_deltas(item['deltas'])}</div>
            </div>
        """
    st.markdown(html, unsafe_allow_html=True)


def render():
    user = usuario_atual()
    if user is None:
        return

    st.markdown(
        f"""
        <div class="delta-header">
            <div class="delta-logo">Ranking</div>
            <div class="delta-balance">⚡ {formatar_deltas(user.deltas)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    pos = posicao_do_usuario(user)
    ranking_geral = gerar_ranking(user)
    ranking_curso = ranking_por_curso(user)

    pos_curso = next((i["posicao"] for i in ranking_curso if i.get("eh_voce")), None)
    indice_local = next((idx for idx, i in enumerate(ranking_curso) if i.get("eh_voce")), None)
    pos_curso_label = (
        next((j + 1 for j, i in enumerate(ranking_curso) if i.get("eh_voce")), "—")
    )

    st.markdown(
        f"""
        <div class="delta-hero">
            <h2>Sua posição na UFRJ 🏆</h2>
            <p>Compita com colegas que também estão estudando Cálculo I.</p>
            <div class="delta-hero-stats">
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">#{pos}</div>
                    <div class="delta-hero-stat-label">Geral</div>
                </div>
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">#{pos_curso_label}</div>
                    <div class="delta-hero-stat-label">No curso</div>
                </div>
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">{formatar_deltas(user.deltas_totais)}</div>
                    <div class="delta-hero-stat-label">Total ganho</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    aba = st.radio(
        "Filtro",
        ["🌍 Geral", f"{emoji_curso(user.curso)} Meu curso"],
        horizontal=True,
        label_visibility="collapsed",
    )

    if aba.startswith("🌍"):
        _render_lista(ranking_geral)
    else:
        # renumera as posições só dentro do filtro
        filtrado = []
        for j, item in enumerate(ranking_curso, start=1):
            copia = dict(item)
            copia["posicao"] = j
            filtrado.append(copia)
        _render_lista(filtrado)
