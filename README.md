# Delta — Hackathon UFRJ

Plataforma gamificada de apoio ao estudo de **Cálculo I**.
Combina **Learn Reels** (vídeos curtos), exercícios rápidos, trilhas
personalizadas por curso e um sistema de recompensas reais lastreadas
na moeda interna **Deltas (Δ)**.

> _"Estude Cálculo, acumule Deltas e troque por vantagens reais."_

---

## ⚡ Como rodar

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Rodar o app
streamlit run app.py
```

O app abre em `http://localhost:8501`.

---

## 🗂️ Estrutura

```
Delta/
├── app.py                       # entry point (streamlit run app.py)
├── requirements.txt
├── README.md
└── src/
    ├── app.py                   # configura página, CSS, rotas
    ├── data/                    # catálogos (cursos, reels, exercícios, recompensas, missões)
    ├── models/                  # classes de domínio (Usuario, Missao, etc.)
    ├── services/                # regras de negócio (gamificação, ranking, resgates...)
    ├── pages/                   # telas do app (home, reels, exercícios, loja, ranking, perfil)
    ├── utils/                   # helpers e session_state
    └── styles/style.css         # identidade visual (estilo Instagram/TikTok)
```

---

## ✨ Funcionalidades do MVP

- **Onboarding** — nome, curso e interesses → bônus de boas-vindas (20 Δ).
- **Home personalizada** — saudação por curso, stories de temas de Cálculo,
  feed "Pra você", recompensa em destaque com barra de progresso, missões
  ativas e exercícios sugeridos.
- **Learn Reels** — feed estilo TikTok, navegação por reel, recompensa ao
  assistir.
- **Exercícios** — quiz com feedback imediato, explicação do gabarito,
  Deltas ao acertar.
- **Loja de Deltas** — recompensas categorizadas; "disponíveis pra você" e
  "próximas conquistas"; gera recibo no resgate.
- **Ranking** — geral e por curso, com posição do aluno em destaque.
- **Perfil** — nível (calouro → mestre delta), estatísticas, missões
  concluídas e info do projeto.

---

## 🧠 Personalização

A camada `src/services/personalizacao.py` cruza:

1. Curso do aluno (filtra reels/exercícios diretos da área)
2. Interesses (esportes, jogos, finanças, cultura geek...)
3. Conteúdo geral como fallback

Resultado: o feed da Home já abre com material aderente ao perfil — usando
**marketing de prontidão**: recompensa próxima visível, progresso medido,
ofensiva diária.

---

## 🎨 Design

Inspirado em redes sociais modernas:

- Paleta gradiente roxo/rosa/coral (`#6C5CE7 → #FF6B9D → #FFB86C`)
- Tipografia Inter, peso forte em títulos
- Cards arredondados (16–24px), sombras suaves
- Stories no topo, hero com glassmorphism, carrossel horizontal
- Navbar inferior com 5 abas

CSS centralizado em `src/styles/style.css`.

---

## 🛠️ Stack

- Python 3.10+
- Streamlit
- Sem banco de dados — estado vive na sessão (ideal para o MVP)

---

## 📋 Próximos passos (pós-Hackathon)

- Persistência (Postgres/SQLite)
- Vídeos reais nos Learn Reels (atualmente são placeholders visuais)
- Sistema de pré-requisitos em grafo (limites → derivadas → integrais)
- Login institucional UFRJ
- Painel administrativo para análise discente
