# src/pages/home.py
"""
Home do Delta — feed personalizado estilo Instagram.

Foco: marketing de prontidão. Já na primeira tela aparecem:
- O nome e ofensiva do aluno (engajamento)
- Stories de temas de Cálculo (curiosidade, reels rápidos)
- Hero personalizado por curso
- Carrossel "Pra você" com Learn Reels do curso/interesses
- Recompensa em destaque (gatilho de aspiração)
- Missões em andamento (gatilho de progressão)
- Exercícios sugeridos
"""

import streamlit as st

from src.utils.session_state import usuario_atual, ir_para
from src.utils.helpers import formatar_deltas, emoji_curso, emoji_tema, truncar
from src.services.personalizacao import feed_personalizado, exercicios_personalizados, temas_relevantes
from src.services.progresso import estatisticas_usuario
from src.services.gamificacao import calcular_nivel, avaliar_missoes
from src.data.recompensas import obter_recompensa_em_destaque, listar_recompensas_acessiveis
from src.data.missoes import listar_missoes


def render():
    user = usuario_atual()
    if user is None:
        return

    # Atualiza missões antes de renderizar
    novas = avaliar_missoes(user)
    if novas:
        st.session_state.missoes_concluidas_recente.extend([m.id for m in novas])
        for m in novas:
            st.toast(f"🎉 Missão concluída: {m.titulo} (+{m.premio_deltas} Deltas)", icon="🏆")

    nivel_nome, nivel_emoji = calcular_nivel(user.deltas_totais)
    stats = estatisticas_usuario(user)

    # ============ HEADER ============
    st.markdown(
        f"""
        <div class="delta-header">
            <div class="delta-logo">Delta</div>
            <div class="delta-balance">⚡ {formatar_deltas(user.deltas)} Deltas</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ============ STORIES (temas de Cálculo) ============
    temas = temas_relevantes(user)[:6]
    stories_html = '<div class="delta-stories">'
    # Story do próprio usuário
    iniciais = "".join([w[0] for w in user.nome.split()[:2]]).upper() or "Δ"
    stories_html += f'''
        <div class="delta-story">
            <div class="delta-story-ring">
                <div class="delta-story-inner">{iniciais}</div>
            </div>
            <div class="delta-story-label">Você</div>
        </div>
    '''
    for tema in temas:
        stories_html += f'''
            <div class="delta-story">
                <div class="delta-story-ring">
                    <div class="delta-story-inner">{emoji_tema(tema.split()[0])}</div>
                </div>
                <div class="delta-story-label">{truncar(tema, 14)}</div>
            </div>
        '''
    stories_html += "</div>"
    st.markdown(stories_html, unsafe_allow_html=True)

    # ============ HERO ============
    st.markdown(
        f"""
        <div class="delta-hero">
            <h2>Olá, {user.nome.split()[0]}! {nivel_emoji}</h2>
            <p>Trilha de Cálculo I personalizada para <b>{emoji_curso(user.curso)} {user.curso}</b></p>
            <div class="delta-hero-stats">
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">🔥 {user.sequencia_dias}</div>
                    <div class="delta-hero-stat-label">Dias seguidos</div>
                </div>
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">{nivel_emoji}</div>
                    <div class="delta-hero-stat-label">{nivel_nome}</div>
                </div>
                <div class="delta-hero-stat">
                    <div class="delta-hero-stat-value">{stats['exercicios_acertados']}</div>
                    <div class="delta-hero-stat-label">Acertos</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ============ AÇÃO RÁPIDA ============
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🎬 Reels", use_container_width=True):
            ir_para("Learn Reels")
            st.rerun()
    with col2:
        if st.button("✏️ Praticar", use_container_width=True):
            ir_para("Exercícios")
            st.rerun()
    with col3:
        if st.button("🏆 Loja", use_container_width=True):
            ir_para("Loja")
            st.rerun()

    # ============ CARROSSEL "PRA VOCÊ" ============
    st.markdown(
        """
        <div class="delta-section-title">
            <h3>✨ Pra você</h3>
            <span class="badge">Personalizado</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    feed = feed_personalizado(user, limite=6)
    if feed:
        carrossel_html = '<div class="delta-h-scroll">'
        for reel in feed:
            assistido = "✓ visto" if reel["id"] in user.reels_assistidos else f"+{reel['recompensa_deltas']}Δ"
            carrossel_html += f'''
                <div class="delta-mini-card">
                    <div class="delta-mini-card-thumb">{emoji_tema(reel['tema_calculo'])}</div>
                    <div class="delta-mini-card-title">{truncar(reel['titulo'], 50)}</div>
                    <div class="delta-mini-card-meta">{reel['duracao_segundos']}s · {assistido}</div>
                </div>
            '''
        carrossel_html += "</div>"
        st.markdown(carrossel_html, unsafe_allow_html=True)

        if st.button("Ver todos os reels →", key="all_reels", use_container_width=True):
            ir_para("Learn Reels")
            st.rerun()

    # ============ RECOMPENSA EM DESTAQUE ============
    destaque = obter_recompensa_em_destaque(user.deltas)
    acessiveis = listar_recompensas_acessiveis(user.deltas)

    st.markdown(
        """
        <div class="delta-section-title">
            <h3>🎁 Sua próxima recompensa</h3>
            <span class="badge">{}</span>
        </div>
        """.format(f"{len(acessiveis)} disponíveis" if acessiveis else "em breve"),
        unsafe_allow_html=True,
    )

    if destaque:
        progresso = min(user.deltas / destaque["custo_deltas"], 1.0) if destaque["custo_deltas"] > 0 else 1.0
        progresso_pct = int(progresso * 100)
        falta = max(destaque["custo_deltas"] - user.deltas, 0)
        status_msg = (
            f"Você já pode resgatar! 🔥"
            if falta == 0
            else f"Faltam <b>{falta} Deltas</b> ({progresso_pct}%)"
        )

        st.markdown(
            f"""
            <div class="delta-reward-card">
                <div class="delta-reward-icon">{destaque.get('icone', '🎁')}</div>
                <div class="delta-reward-info">
                    <div class="delta-reward-name">{destaque['nome']}</div>
                    <div class="delta-reward-desc">{destaque['descricao']}</div>
                    <div style="margin-top:6px;">
                        <span class="delta-reward-cost">⚡ {destaque['custo_deltas']}</span>
                        <span style="font-size:11px;color:var(--delta-text-soft);margin-left:8px;">{status_msg}</span>
                    </div>
                    <div class="delta-progress-bar" style="margin-top:8px;">
                        <div class="delta-progress-fill" style="width:{progresso_pct}%;"></div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Ver loja completa →", key="goto_loja", use_container_width=True):
            ir_para("Loja")
            st.rerun()

    # ============ MISSÕES ============
    st.markdown(
        """
        <div class="delta-section-title">
            <h3>🎯 Missões em andamento</h3>
            <span class="badge">{} ativas</span>
        </div>
        """.format(len([m for m in listar_missoes() if not m.concluida])),
        unsafe_allow_html=True,
    )

    for missao in listar_missoes()[:3]:
        progresso_pct = int(missao.progresso_percentual() * 100)
        css_class = "delta-mission concluida" if missao.concluida else "delta-mission"
        check = "✅ " if missao.concluida else ""
        st.markdown(
            f"""
            <div class="{css_class}">
                <div class="delta-mission-header">
                    <div class="delta-mission-title">{check}{missao.titulo}</div>
                    <div class="delta-mission-prize">+{missao.premio_deltas} Δ</div>
                </div>
                <div class="delta-mission-desc">{missao.descricao}</div>
                <div class="delta-progress-bar">
                    <div class="delta-progress-fill" style="width:{progresso_pct}%;"></div>
                </div>
                <div style="font-size:11px;color:var(--delta-text-soft);margin-top:6px;">
                    {missao.progresso_atual} / {missao.objetivo_contagem}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ============ EXERCÍCIO RELÂMPAGO ============
    st.markdown(
        """
        <div class="delta-section-title">
            <h3>⚡ Pratique agora</h3>
            <span class="badge">Ganhe Deltas</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    exs = exercicios_personalizados(user, limite=3)
    if exs:
        for ex in exs[:2]:
            ja_acertou = ex["id"] in user.exercicios_acertados
            badge = "✅ Acertado" if ja_acertou else f"+{ex['recompensa_deltas']} Δ"
            st.markdown(
                f"""
                <div class="delta-exercise-card">
                    <div class="delta-exercise-meta">
                        <span class="delta-tag">{emoji_tema(ex['tema_calculo'])} {ex['tema_calculo']}</span>
                        <span class="delta-tag">{ex['dificuldade']}</span>
                        <span class="delta-tag">{badge}</span>
                    </div>
                    <div class="delta-exercise-question">{truncar(ex['pergunta'], 120)}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        if st.button("Resolver exercícios →", key="goto_ex", use_container_width=True, type="primary"):
            ir_para("Exercícios")
            st.rerun()
