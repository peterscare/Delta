# src/data/ranking_base.py
"""
Base fictícia de alunos para o ranking do Delta.

No MVP do Hackathon o ranking não consulta um backend real — usamos
uma lista de "personagens" de outros estudantes para que o usuário
veja sua posição e sinta o lado social/competitivo do app.
"""

RANKING_BASE = [
    {"nome": "Ana C.",     "curso": "Engenharia Civil",            "deltas": 980},
    {"nome": "Pedro M.",   "curso": "Ciência da Computação",       "deltas": 870},
    {"nome": "Júlia R.",   "curso": "Engenharia Mecânica",         "deltas": 760},
    {"nome": "Lucas T.",   "curso": "Engenharia Elétrica",         "deltas": 690},
    {"nome": "Marina S.",  "curso": "Matemática",                  "deltas": 640},
    {"nome": "Rafael L.",  "curso": "Engenharia Química",          "deltas": 580},
    {"nome": "Beatriz O.", "curso": "Física",                      "deltas": 520},
    {"nome": "Diego A.",   "curso": "Engenharia de Produção",      "deltas": 450},
    {"nome": "Camila F.",  "curso": "Estatística",                 "deltas": 380},
    {"nome": "Thiago P.",  "curso": "Ciência da Computação",       "deltas": 320},
    {"nome": "Larissa D.", "curso": "Engenharia Civil",            "deltas": 260},
    {"nome": "Gabriel N.", "curso": "Outro curso de exatas",       "deltas": 180},
]


def obter_ranking_base():
    return list(RANKING_BASE)
