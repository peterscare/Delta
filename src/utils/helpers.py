# src/utils/helpers.py
"""Helpers gerais do Delta."""


def formatar_deltas(valor):
    """Formata valor de Deltas com separador de milhar."""
    try:
        return f"{int(valor):,}".replace(",", ".")
    except (TypeError, ValueError):
        return "0"


def truncar(texto, tamanho=80):
    if not texto:
        return ""
    if len(texto) <= tamanho:
        return texto
    return texto[: tamanho - 1].rstrip() + "…"


def emoji_curso(nome_curso):
    """Retorna um emoji característico do curso."""
    mapa = {
        "Engenharia Civil": "🏗️",
        "Engenharia Mecânica": "⚙️",
        "Engenharia Elétrica": "⚡",
        "Engenharia de Produção": "📊",
        "Engenharia Química": "🧪",
        "Ciência da Computação": "💻",
        "Matemática": "🧮",
        "Física": "🔭",
        "Estatística": "📈",
        "Outro curso de exatas": "🎓",
    }
    return mapa.get(nome_curso, "🎓")


def emoji_tema(tema):
    mapa = {
        "Limites": "🎯",
        "Continuidade": "🔗",
        "Derivadas": "📐",
        "Integrais": "∫",
        "Funções": "📊",
        "Otimização": "🚀",
        "Taxas de variação": "⏱️",
    }
    return mapa.get(tema, "📚")
