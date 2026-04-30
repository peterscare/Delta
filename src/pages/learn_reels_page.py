# src/pages/learn_reels_page.py
"""
Tela de Learn Reels — estilo feed de reels.

Card grande, swipe simulado por botão "Próximo", recompensa imediata.
"""

import streamlit as st

from src.utils.session_state import usuario_atual
from src.utils.helpers import emoji_tema, formatar_deltas
from src.services.personalizacao import feed_personalizado


def render():
    user = usuario_atual()
    if user is None:
        return

    st.markdown(
        f"""
        <div class="delta-header">
            <div class="delta-logo">Reels</div>
            <div class="delta-balance">⚡ {formatar_deltas(user.deltas)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    feed = feed_personalizado(user, limite=15)
    if not feed:
        st.info("Nenhum reel disponível por enquanto.")
        return

    # Mantém posição no feed
    if "reel_index" not in st.session_state:
        st.session_state.reel_index = 0

    if st.session_state.reel_index >= len(feed):
        st.session_state.reel_index = 0

    reel = feed[st.session_state.reel_index]
    ja_assistido = reel["id"] in user.reels_assistidos

    # Card do reel atual (grande)
    interesses_html = "".join(
        [f'<span class="delta-tag">#{i.lower()}</span>' for i in reel.get("interesses", [])[:3]]
    )

    st.markdown(
        f"""
        <div class="delta-reel-card">
            <div class="delta-reel-thumb">
                {emoji_tema(reel['tema_calculo'])}
                <span class="delta-reel-duration">▶ {reel['duracao_segundos']}s</span>
            </div>
            <div class="delta-reel-info">
                <div class="delta-reel-title">{reel['titulo']}</div>
                <div class="delta-reel-desc">{reel['descricao']}</div>
                <div class="delta-reel-tags">
                    <span class="delta-tag">{emoji_tema(reel['tema_calculo'])} {reel['tema_calculo']}</span>
                    <span class="delta-tag">📚 {reel['curso']}</span>
                    {interesses_html}
                </div>
                <div class="delta-reel-footer">
                    <span style="font-size:12px;color:var(--delta-text-soft);">
                        {st.session_state.reel_index + 1} de {len(feed)}
                    </span>
                    <span class="delta-reel-reward">
                        ⚡ {'já ganho' if ja_assistido else f'+{reel["recompensa_deltas"]} Deltas'}
                    </span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_a, col_b, col_c = st.columns([1, 2, 1])

    with col_a:
        if st.button("⬅️", key="reel_prev", use_container_width=True, disabled=st.session_state.reel_index == 0):
            st.session_state.reel_index = max(0, st.session_state.reel_index - 1)
            st.rerun()

    with col_b:
        label = "✅ Já assisti" if ja_assistido else f"▶️ Assistir (+{reel['recompensa_deltas']} Δ)"
        if st.button(label, key="reel_watch", use_container_width=True, type="primary", disabled=ja_assistido):
            user.registrar_reel(reel["id"], reel["recompensa_deltas"])
            st.toast(f"+{reel['recompensa_deltas']} Deltas! 🎉", icon="⚡")
            st.session_state.reel_index = (st.session_state.reel_index + 1) % len(feed)
            st.rerun()

    with col_c:
        if st.button("➡️", key="reel_next", use_container_width=True):
            st.session_state.reel_index = (st.session_state.reel_index + 1) % len(feed)
            st.rerun()

    # Listagem completa abaixo (estilo "explorar")
    st.markdown(
        """
        <div class="delta-section-title">
            <h3>🔍 Explorar mais</h3>
            <span class="badge">Todos os reels</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

   grid_html = '<div class="delta-h-scroll">'
    for i, r in enumerate(feed):
        if i == st.session_state.reel_index:
            continue
        assistido = "✓ visto" if r["id"] in user.reels_assistidos else f"+{r['recompensa_deltas']}Δ"
        grid_html += f'<div class="delta-mini-card"><div class="delta-mini-card-thumb">{emoji_tema(r["tema_calculo"])}</div><div class="delta-mini-card-title">{r["titulo"][:48]}</div><div class="delta-mini-card-meta">{r["duracao_segundos"]}s · {assistido}</div></div>'
    grid_html += "</div>"
    grid_html += "</div>"
    st.markdown(grid_html, unsafe_allow_html=True)
