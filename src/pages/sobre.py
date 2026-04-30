# src/pages/sobre.py
"""Perfil + sobre o projeto."""

import streamlit as st

from src.utils.session_state import usuario_atual, deslogar
from src.utils.helpers import formatar_deltas, emoji_curso
from src.services.progresso import estatisticas_usuario
from src.services.gamificacao import calcular_nivel
from src.data.missoes import listar_missoes


def render():
    user = usuario_atual()
    if user is None:
        return

    stats = estatisticas_usuario(user)
    nivel_nome, nivel_emoji = calcular_nivel(user.deltas_totais)
    iniciais = "".join(p[0] for p in user.nome.split()[:2]).upper() or "Δ"

    st.markdown(
        f"""
        <div class="delta-header">
            <div class="delta-logo">Perfil</div>
            <div class="delta-balance">⚡ {formatar_deltas(user.deltas)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Card do perfil
    st.markdown(
        f"""
        <div class="delta-hero" style="text-align:center;">
            <div style="display:flex;justify-content:center;margin-bottom:12px;">
                <div style="width:72px;height:72px;border-radius:50%;background:rgba(255,255,255,0.25);display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:900;color:white;border:3px solid rgba(255,255,255,0.6);">
                    {iniciais}
                </div>
            </div>
            <h2>{user.nome}</h2>
            <p>{emoji_curso(user.curso)} {user.curso} · {nivel_emoji} {nivel_nome}</p>
            <div class="delta-hero-stats">
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">{user.sequencia_dias}🔥</div>
                    <div class="delta-hero-stat-label">Sequência</div>
                </div>
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">{formatar_deltas(user.deltas_totais)}</div>
                    <div class="delta-hero-stat-label">Total Δ</div>
                </div>
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">{len(user.missoes_concluidas)}</div>
                    <div class="delta-hero-stat-label">Missões</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Estatísticas
    st.markdown('<div class="delta-section-title"><h3>📊 Estatísticas</h3></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.metric("Reels assistidos", f"{stats['reels_assistidos']}/{stats['total_reels']}")
    col2.metric("Exercícios feitos", f"{stats['exercicios_feitos']}/{stats['total_exercicios']}")
    col1.metric("Acertos", stats["exercicios_acertados"])
    col2.metric("Taxa de acerto", f"{int(stats['taxa_acerto']*100)}%")

    # Interesses
    if user.interesses:
        st.markdown('<div class="delta-section-title"><h3>💡 Seus interesses</h3></div>', unsafe_allow_html=True)
        chips = "".join([f'<span class="delta-chip">#{i.lower()}</span>' for i in user.interesses])
        st.markdown(f"<div>{chips}</div>", unsafe_allow_html=True)

    # Missões concluídas
    concluidas = [m for m in listar_missoes() if m.concluida]
    if concluidas:
        st.markdown('<div class="delta-section-title"><h3>🏆 Missões concluídas</h3></div>', unsafe_allow_html=True)
        for m in concluidas:
            st.markdown(
                f"""
                <div class="delta-mission concluida">
                    <div class="delta-mission-header">
                        <div class="delta-mission-title">✅ {m.titulo}</div>
                        <div class="delta-mission-prize">+{m.premio_deltas} Δ</div>
                    </div>
                    <div class="delta-mission-desc">{m.descricao}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Sobre o projeto
    st.markdown('<div class="delta-section-title"><h3>ℹ️ Sobre o Delta</h3></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="delta-about-card">
            <h4>O que é o Delta?</h4>
            <p>Plataforma gamificada de apoio ao estudo de Cálculo I, desenvolvida para o
            Hackathon UFRJ. Combina <b>Learn Reels</b>, exercícios curtos, trilhas
            personalizadas por curso e recompensas reais via parceria institucional.</p>
        </div>
        <div class="delta-about-card">
            <h4>Como funciona a moeda?</h4>
            <p>Os <b>Deltas</b> são acumulados ao assistir reels, acertar exercícios,
            manter sequência diária e concluir missões. Eles podem ser trocados na loja
            por vantagens acadêmicas e benefícios institucionais.</p>
        </div>
        <div class="delta-about-card">
            <h4>Por que esse nome?</h4>
            <p>Δ (delta) é o símbolo de variação em matemática — a essência do Cálculo I.
            Curto, fácil de lembrar e conectado ao universo da disciplina.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Sair
    st.markdown("---")
    if st.button("Sair", use_container_width=True):
        deslogar()
        st.rerun()
