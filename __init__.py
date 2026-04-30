# src/pages/loja.py
"""Loja de Deltas — recompensas em destaque e por categoria."""

import streamlit as st

from src.utils.session_state import usuario_atual
from src.utils.helpers import formatar_deltas
from src.data.recompensas import (
    listar_recompensas_ativas,
    listar_recompensas_acessiveis,
)
from src.services.resgates import efetuar_resgate


def _card_recompensa(r, user):
    pode = user.deltas >= r["custo_deltas"]
    progresso_pct = min(int(user.deltas / r["custo_deltas"] * 100), 100) if r["custo_deltas"] > 0 else 100

    st.markdown(
        f"""
        <div class="delta-reward-card">
            <div class="delta-reward-icon">{r.get('icone', '🎁')}</div>
            <div class="delta-reward-info">
                <div class="delta-reward-name">{r['nome']}</div>
                <div class="delta-reward-desc">{r['descricao']}</div>
                <div style="margin-top:6px;display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
                    <span class="delta-reward-cost">⚡ {r['custo_deltas']}</span>
                    <span class="delta-tag">{r['tipo']}</span>
                </div>
                <div class="delta-progress-bar" style="margin-top:8px;">
                    <div class="delta-progress-fill" style="width:{progresso_pct}%;"></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    label = "Resgatar 🎁" if pode else f"Faltam {r['custo_deltas'] - user.deltas} Δ"
    if st.button(label, key=f"resgate_{r['id']}", use_container_width=True, disabled=not pode, type="primary" if pode else "secondary"):
        resultado = efetuar_resgate(user, r["id"])
        if resultado["sucesso"]:
            st.success(f"🎉 {resultado['mensagem']}\n\n**Recibo:** `{resultado['recibo']['id_recibo']}`")
            st.balloons()
        else:
            st.error(resultado["mensagem"])
        st.rerun()


def render():
    user = usuario_atual()
    if user is None:
        return

    st.markdown(
        f"""
        <div class="delta-header">
            <div class="delta-logo">Loja</div>
            <div class="delta-balance">⚡ {formatar_deltas(user.deltas)} Deltas</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    todas = listar_recompensas_ativas()
    acessiveis = listar_recompensas_acessiveis(user.deltas)

    # Hero
    st.markdown(
        f"""
        <div class="delta-hero">
            <h2>Sua moeda, suas vantagens 🎁</h2>
            <p>Use seus Deltas em recompensas reais da UFRJ.</p>
            <div class="delta-hero-stats">
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">{formatar_deltas(user.deltas)}</div>
                    <div class="delta-hero-stat-label">Saldo</div>
                </div>
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">{len(acessiveis)}</div>
                    <div class="delta-hero-stat-label">Disponíveis</div>
                </div>
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">{len(user.recompensas_resgatadas)}</div>
                    <div class="delta-hero-stat-label">Resgatadas</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Disponíveis agora
    if acessiveis:
        st.markdown(
            """
            <div class="delta-section-title">
                <h3>🔥 Disponíveis pra você</h3>
                <span class="badge">Resgate agora</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for r in sorted(acessiveis, key=lambda x: -x["custo_deltas"]):
            _card_recompensa(r, user)

    # Por categoria
    categorias = {}
    for r in todas:
        if r in acessiveis:
            continue
        categorias.setdefault(r["tipo"], []).append(r)

    if categorias:
        st.markdown(
            """
            <div class="delta-section-title">
                <h3>🎯 Próximas conquistas</h3>
                <span class="badge">Continue acumulando</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for tipo, lista in sorted(categorias.items(), key=lambda x: min(r["custo_deltas"] for r in x[1])):
            st.markdown(f"**{tipo}**")
            for r in sorted(lista, key=lambda x: x["custo_deltas"]):
                _card_recompensa(r, user)

    # Histórico
    if user.recompensas_resgatadas:
        st.markdown(
            """
            <div class="delta-section-title">
                <h3>📜 Suas conquistas</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for recibo in reversed(user.recompensas_resgatadas[-5:]):
            st.markdown(
                f"""
                <div class="delta-reward-card">
                    <div class="delta-reward-icon">✅</div>
                    <div class="delta-reward-info">
                        <div class="delta-reward-name">{recibo['nome']}</div>
                        <div class="delta-reward-desc">Resgatado em {recibo['data']} · custo {recibo['custo']} Δ</div>
                        <div style="font-size:11px;color:var(--delta-text-soft);margin-top:4px;font-family:monospace;">
                            {recibo['id_recibo']}
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
