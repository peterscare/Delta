/* src/styles/style.css */
/* Identidade visual Delta - inspirada em redes sociais modernas (Instagram, TikTok) */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

/* ========== VARIÁVEIS DE COR ========== */
:root {
    --delta-primary: #6C5CE7;        /* roxo Delta */
    --delta-secondary: #00D4AA;      /* verde menta */
    --delta-accent: #FF6B9D;         /* rosa coral */
    --delta-gradient: linear-gradient(135deg, #6C5CE7 0%, #FF6B9D 50%, #FFB86C 100%);
    --delta-gradient-soft: linear-gradient(135deg, rgba(108, 92, 231, 0.1) 0%, rgba(255, 107, 157, 0.1) 100%);
    --delta-dark: #1a1a2e;
    --delta-card: #ffffff;
    --delta-bg: #fafafa;
    --delta-text: #262626;
    --delta-text-soft: #8e8e8e;
    --delta-border: #efefef;
}

/* ========== BASE ========== */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.stApp {
    background: var(--delta-bg);
}

/* Esconde menu padrão do Streamlit pra ficar mais "app" */
#MainMenu, footer, header[data-testid="stHeader"] {
    visibility: hidden;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 5rem !important;
    max-width: 720px !important;
}

/* ========== HEADER DELTA ========== */
.delta-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 0 16px 0;
    border-bottom: 1px solid var(--delta-border);
    margin-bottom: 20px;
}

.delta-logo {
    font-size: 28px;
    font-weight: 900;
    background: var(--delta-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -1px;
}

.delta-logo::before {
    content: "Δ ";
    -webkit-text-fill-color: initial;
    background: none;
}

.delta-balance {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--delta-gradient);
    color: white;
    padding: 8px 16px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 14px;
    box-shadow: 0 4px 12px rgba(108, 92, 231, 0.3);
}

/* ========== STORIES (TOP) ========== */
.delta-stories {
    display: flex;
    gap: 14px;
    overflow-x: auto;
    padding: 4px 0 16px 0;
    scrollbar-width: none;
}
.delta-stories::-webkit-scrollbar { display: none; }

.delta-story {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-width: 72px;
    cursor: pointer;
}

.delta-story-ring {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: var(--delta-gradient);
    padding: 3px;
    margin-bottom: 6px;
}

.delta-story-inner {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    border: 2px solid white;
}

.delta-story-label {
    font-size: 11px;
    color: var(--delta-text);
    font-weight: 500;
    text-align: center;
    line-height: 1.2;
    max-width: 72px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

/* ========== HERO PERSONALIZADO ========== */
.delta-hero {
    background: var(--delta-gradient);
    border-radius: 24px;
    padding: 24px;
    color: white;
    margin-bottom: 20px;
    box-shadow: 0 8px 24px rgba(108, 92, 231, 0.25);
    position: relative;
    overflow: hidden;
}

.delta-hero::before {
    content: "";
    position: absolute;
    top: -40px;
    right: -40px;
    width: 160px;
    height: 160px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
}

.delta-hero h2 {
    font-size: 22px;
    font-weight: 800;
    margin: 0 0 4px 0;
    color: white;
}

.delta-hero p {
    font-size: 14px;
    opacity: 0.95;
    margin: 0;
    color: white;
}

.delta-hero-stats {
    display: flex;
    gap: 16px;
    margin-top: 16px;
    position: relative;
    z-index: 1;
}

.delta-hero-stat {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    border-radius: 12px;
    padding: 10px 14px;
    flex: 1;
    text-align: center;
}

.delta-hero-stat-value {
    font-size: 20px;
    font-weight: 800;
    color: white;
}

.delta-hero-stat-label {
    font-size: 11px;
    opacity: 0.9;
    color: white;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* ========== SEÇÕES ========== */
.delta-section-title {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 24px 0 12px 0;
}

.delta-section-title h3 {
    font-size: 17px;
    font-weight: 800;
    color: var(--delta-text);
    margin: 0;
}

.delta-section-title .badge {
    background: var(--delta-gradient-soft);
    color: var(--delta-primary);
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* ========== CARD REEL ========== */
.delta-reel-card {
    background: var(--delta-card);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
    margin-bottom: 16px;
    transition: transform 0.2s, box-shadow 0.2s;
}

.delta-reel-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.delta-reel-thumb {
    height: 200px;
    background: var(--delta-gradient);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 64px;
    color: white;
    position: relative;
}

.delta-reel-thumb::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, transparent 60%, rgba(0,0,0,0.5) 100%);
}

.delta-reel-duration {
    position: absolute;
    bottom: 12px;
    right: 12px;
    background: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 600;
    z-index: 1;
}

.delta-reel-info {
    padding: 14px 16px 16px 16px;
}

.delta-reel-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--delta-text);
    margin: 0 0 4px 0;
    line-height: 1.3;
}

.delta-reel-desc {
    font-size: 13px;
    color: var(--delta-text-soft);
    line-height: 1.4;
    margin: 0 0 10px 0;
}

.delta-reel-tags {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
    margin-bottom: 10px;
}

.delta-tag {
    background: var(--delta-gradient-soft);
    color: var(--delta-primary);
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 600;
}

.delta-reel-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 10px;
    border-top: 1px solid var(--delta-border);
}

.delta-reel-reward {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    color: var(--delta-secondary);
    font-weight: 700;
    font-size: 13px;
}

/* ========== CARD EXERCÍCIO ========== */
.delta-exercise-card {
    background: var(--delta-card);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
    margin-bottom: 16px;
    border-left: 4px solid var(--delta-primary);
}

.delta-exercise-meta {
    display: flex;
    gap: 8px;
    margin-bottom: 12px;
}

.delta-exercise-question {
    font-size: 16px;
    font-weight: 600;
    color: var(--delta-text);
    line-height: 1.5;
    margin-bottom: 16px;
}

/* ========== CARD RECOMPENSA ========== */
.delta-reward-card {
    background: var(--delta-card);
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
    margin-bottom: 12px;
    display: flex;
    gap: 14px;
    align-items: center;
    transition: transform 0.2s;
}

.delta-reward-card:hover {
    transform: translateX(4px);
}

.delta-reward-icon {
    width: 56px;
    height: 56px;
    border-radius: 16px;
    background: var(--delta-gradient-soft);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    flex-shrink: 0;
}

.delta-reward-info {
    flex: 1;
}

.delta-reward-name {
    font-size: 15px;
    font-weight: 700;
    color: var(--delta-text);
    margin: 0 0 2px 0;
}

.delta-reward-desc {
    font-size: 12px;
    color: var(--delta-text-soft);
    line-height: 1.4;
    margin: 0 0 6px 0;
}

.delta-reward-cost {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: var(--delta-gradient);
    color: white;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
}

/* ========== MISSÃO ========== */
.delta-mission {
    background: var(--delta-card);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    border: 1px solid var(--delta-border);
}

.delta-mission.concluida {
    background: linear-gradient(135deg, rgba(0, 212, 170, 0.1), rgba(108, 92, 231, 0.1));
    border-color: var(--delta-secondary);
}

.delta-mission-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
}

.delta-mission-title {
    font-size: 14px;
    font-weight: 700;
    color: var(--delta-text);
    margin: 0;
}

.delta-mission-prize {
    font-size: 12px;
    font-weight: 700;
    color: var(--delta-secondary);
}

.delta-mission-desc {
    font-size: 12px;
    color: var(--delta-text-soft);
    line-height: 1.4;
    margin: 0 0 10px 0;
}

.delta-progress-bar {
    height: 6px;
    background: var(--delta-border);
    border-radius: 999px;
    overflow: hidden;
}

.delta-progress-fill {
    height: 100%;
    background: var(--delta-gradient);
    border-radius: 999px;
    transition: width 0.4s ease;
}

/* ========== RANKING ========== */
.delta-ranking-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 14px;
    background: var(--delta-card);
    border-radius: 14px;
    margin-bottom: 8px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
}

.delta-ranking-item.eh-voce {
    background: var(--delta-gradient);
    color: white;
    box-shadow: 0 6px 18px rgba(108, 92, 231, 0.3);
}

.delta-ranking-item.eh-voce .delta-ranking-name,
.delta-ranking-item.eh-voce .delta-ranking-course {
    color: white;
}

.delta-ranking-position {
    font-size: 18px;
    font-weight: 900;
    width: 32px;
    text-align: center;
}

.delta-ranking-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: var(--delta-gradient-soft);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    color: var(--delta-primary);
    font-weight: 700;
}

.delta-ranking-item.eh-voce .delta-ranking-avatar {
    background: rgba(255, 255, 255, 0.25);
    color: white;
}

.delta-ranking-info {
    flex: 1;
}

.delta-ranking-name {
    font-size: 14px;
    font-weight: 700;
    color: var(--delta-text);
}

.delta-ranking-course {
    font-size: 11px;
    color: var(--delta-text-soft);
}

.delta-ranking-deltas {
    font-weight: 800;
    font-size: 14px;
}

/* ========== BOTÕES ========== */
.stButton > button {
    width: 100%;
    border-radius: 14px !important;
    font-weight: 700 !important;
    padding: 10px 16px !important;
    border: 1px solid var(--delta-border) !important;
    background: white !important;
    color: var(--delta-text) !important;
    transition: all 0.2s !important;
}

.stButton > button:hover {
    background: var(--delta-gradient-soft) !important;
    border-color: var(--delta-primary) !important;
    color: var(--delta-primary) !important;
    transform: translateY(-1px);
}

.stButton > button[kind="primary"] {
    background: var(--delta-gradient) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(108, 92, 231, 0.3) !important;
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(108, 92, 231, 0.4) !important;
}

/* ========== INPUTS ========== */
.stTextInput > div > div > input,
.stSelectbox > div > div {
    border-radius: 12px !important;
    border: 1px solid var(--delta-border) !important;
}

.stRadio > div {
    gap: 8px;
}

.stRadio label {
    background: white;
    padding: 12px 14px !important;
    border-radius: 12px !important;
    border: 1.5px solid var(--delta-border);
    font-weight: 500;
    transition: all 0.2s;
    width: 100%;
}

.stRadio label:hover {
    border-color: var(--delta-primary);
    background: var(--delta-gradient-soft);
}

/* ========== ALERTS ========== */
[data-testid="stAlert"] {
    border-radius: 14px !important;
    border: none !important;
}

/* ========== SIDEBAR ========== */
[data-testid="stSidebar"] {
    background: white;
    border-right: 1px solid var(--delta-border);
}

[data-testid="stSidebar"] .delta-logo {
    margin-bottom: 20px;
    display: block;
    text-align: center;
}

/* ========== TELA DE LOGIN ========== */
.delta-login-hero {
    text-align: center;
    padding: 30px 0 20px 0;
}

.delta-login-hero .delta-bigΔ {
    font-size: 80px;
    background: var(--delta-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    font-weight: 900;
    margin-bottom: 0;
}

.delta-login-hero h1 {
    font-size: 32px;
    font-weight: 900;
    margin: 8px 0 8px 0;
    background: var(--delta-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -1px;
}

.delta-login-hero p {
    font-size: 15px;
    color: var(--delta-text-soft);
    margin: 0 0 24px 0;
    line-height: 1.5;
}

.delta-login-features {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin: 20px 0;
}

.delta-login-feature {
    background: white;
    border-radius: 14px;
    padding: 14px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.delta-login-feature-icon {
    font-size: 28px;
    margin-bottom: 6px;
}

.delta-login-feature-title {
    font-size: 12px;
    font-weight: 700;
    color: var(--delta-text);
    margin-bottom: 2px;
}

.delta-login-feature-desc {
    font-size: 10px;
    color: var(--delta-text-soft);
    line-height: 1.3;
}

/* ========== FEEDBACK ========== */
.delta-feedback-correto {
    background: linear-gradient(135deg, #00D4AA, #00B894);
    color: white;
    border-radius: 16px;
    padding: 16px;
    margin: 16px 0;
    font-weight: 600;
    box-shadow: 0 4px 16px rgba(0, 212, 170, 0.25);
}

.delta-feedback-errado {
    background: linear-gradient(135deg, #FF6B9D, #E84393);
    color: white;
    border-radius: 16px;
    padding: 16px;
    margin: 16px 0;
    font-weight: 600;
    box-shadow: 0 4px 16px rgba(255, 107, 157, 0.25);
}

/* ========== CHIP DE INTERESSE ========== */
.delta-chip {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    background: var(--delta-gradient-soft);
    color: var(--delta-primary);
    font-weight: 600;
    font-size: 13px;
    margin: 4px;
}

/* ========== CARROSSEL HORIZONTAL ========== */
.delta-h-scroll {
    display: flex;
    gap: 12px;
    overflow-x: auto;
    padding-bottom: 8px;
    scrollbar-width: thin;
}

.delta-mini-card {
    min-width: 180px;
    max-width: 180px;
    background: var(--delta-card);
    border-radius: 16px;
    padding: 14px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    flex-shrink: 0;
}

.delta-mini-card-thumb {
    height: 100px;
    border-radius: 12px;
    background: var(--delta-gradient);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 40px;
    color: white;
    margin-bottom: 10px;
}

.delta-mini-card-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--delta-text);
    line-height: 1.3;
    margin-bottom: 4px;
}

.delta-mini-card-meta {
    font-size: 11px;
    color: var(--delta-text-soft);
}

/* ========== SOBRE ========== */
.delta-about-card {
    background: white;
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 14px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.04);
}

.delta-about-card h4 {
    font-size: 16px;
    font-weight: 800;
    color: var(--delta-text);
    margin: 0 0 8px 0;
}

.delta-about-card p {
    font-size: 13px;
    color: var(--delta-text-soft);
    line-height: 1.5;
    margin: 0;
}
