# src/data/recompensas.py
"""
Recompensas do Delta — loja de Deltas.

As recompensas podem ser simbólicas, acadêmicas, institucionais
(sujeitas a parceria com a Escola Politécnica) ou de gamificação.
"""


RECOMPENSAS = [
    {
        "id": 1,
        "nome": "Certificado de participação",
        "descricao": "Certificado simbólico para alunos que participarem ativamente da plataforma Delta.",
        "custo_deltas": 100,
        "tipo": "Acadêmica",
        "icone": "🎓",
        "parceiro": "Projeto Delta",
        "ativa": True,
        "depende_validacao": False,
    },
    {
        "id": 2,
        "nome": "Badge de destaque acadêmico",
        "descricao": "Selo digital para estudantes que mantiverem bom desempenho e constância no uso do aplicativo.",
        "custo_deltas": 150,
        "tipo": "Gamificação",
        "icone": "🏅",
        "parceiro": "Projeto Delta",
        "ativa": True,
        "depende_validacao": False,
    },
    {
        "id": 3,
        "nome": "Participação em sorteio de benefício",
        "descricao": "Entrada simbólica em sorteio de benefício institucional, dependente de regras e validação da universidade.",
        "custo_deltas": 300,
        "tipo": "Institucional",
        "icone": "🎟️",
        "parceiro": "Escola Politécnica da UFRJ",
        "ativa": True,
        "depende_validacao": True,
    },
    {
        "id": 4,
        "nome": "Benefício institucional via parceria",
        "descricao": "Recompensa viabilizada por parceria com a Escola Politécnica da UFRJ, podendo envolver auxílios ou créditos simbólicos.",
        "custo_deltas": 500,
        "tipo": "Institucional",
        "icone": "🏛️",
        "parceiro": "Escola Politécnica da UFRJ",
        "ativa": True,
        "depende_validacao": True,
    },
    {
        "id": 5,
        "nome": "Prioridade simbólica em atividade acadêmica",
        "descricao": "Benefício simbólico que oferece prioridade em inscrições de oficinas, minicursos ou atividades.",
        "custo_deltas": 250,
        "tipo": "Acadêmica",
        "icone": "⭐",
        "parceiro": "Coordenação do Projeto",
        "ativa": True,
        "depende_validacao": True,
    },
    {
        "id": 6,
        "nome": "Cupom Delta",
        "descricao": "Cupom simbólico de engajamento que pode ser usado em ações patrocinadas ou parcerias do projeto.",
        "custo_deltas": 200,
        "tipo": "Parceria",
        "icone": "🎫",
        "parceiro": "Parceiros institucionais",
        "ativa": True,
        "depende_validacao": True,
    },
    {
        "id": 7,
        "nome": "Desafio bônus liberado",
        "descricao": "Liberação de desafios extras que oferecem mais Deltas e aumentam a competitividade.",
        "custo_deltas": 80,
        "tipo": "Gamificação",
        "icone": "🚀",
        "parceiro": "Projeto Delta",
        "ativa": True,
        "depende_validacao": False,
    },
    {
        "id": 8,
        "nome": "Mentoria com veterano",
        "descricao": "Sessão de 30 minutos com um veterano do curso para tirar dúvidas e receber dicas de Cálculo I.",
        "custo_deltas": 350,
        "tipo": "Acadêmica",
        "icone": "👨‍🏫",
        "parceiro": "Centro Acadêmico",
        "ativa": True,
        "depende_validacao": True,
    },
]


def listar_recompensas():
    return RECOMPENSAS


def listar_recompensas_ativas():
    return [r for r in RECOMPENSAS if r["ativa"]]


def buscar_recompensa_por_id(recompensa_id):
    for r in RECOMPENSAS:
        if r["id"] == recompensa_id:
            return r
    return None


def listar_recompensas_por_tipo(tipo):
    return [r for r in RECOMPENSAS if r["tipo"] == tipo]


def listar_recompensas_acessiveis(saldo_deltas):
    """Recompensas que o aluno consegue resgatar com o saldo atual."""
    return [
        r for r in RECOMPENSAS if r["ativa"] and r["custo_deltas"] <= saldo_deltas
    ]


def verificar_se_pode_resgatar(recompensa_id, saldo_deltas):
    r = buscar_recompensa_por_id(recompensa_id)
    if r is None or not r["ativa"]:
        return False
    return saldo_deltas >= r["custo_deltas"]


def resgatar_recompensa(recompensa_id, saldo_deltas):
    """
    Tenta resgatar uma recompensa.
    Retorna {sucesso, mensagem, novo_saldo, recompensa}.
    """
    r = buscar_recompensa_por_id(recompensa_id)

    if r is None:
        return {
            "sucesso": False,
            "mensagem": "Recompensa não encontrada.",
            "novo_saldo": saldo_deltas,
            "recompensa": None,
        }

    if not r["ativa"]:
        return {
            "sucesso": False,
            "mensagem": "Esta recompensa não está disponível no momento.",
            "novo_saldo": saldo_deltas,
            "recompensa": r,
        }

    if saldo_deltas < r["custo_deltas"]:
        return {
            "sucesso": False,
            "mensagem": "Saldo de Deltas insuficiente para resgatar esta recompensa.",
            "novo_saldo": saldo_deltas,
            "recompensa": r,
        }

    novo_saldo = saldo_deltas - r["custo_deltas"]
    mensagem = "Recompensa resgatada com sucesso!"
    if r["depende_validacao"]:
        mensagem += " Esta recompensa depende de validação institucional."

    return {
        "sucesso": True,
        "mensagem": mensagem,
        "novo_saldo": novo_saldo,
        "recompensa": r,
    }


def obter_recompensa_em_destaque(saldo_deltas):
    """Escolhe uma recompensa para destacar na Home."""
    ativas = listar_recompensas_ativas()
    if not ativas:
        return None

    acessiveis = listar_recompensas_acessiveis(saldo_deltas)
    if acessiveis:
        return max(acessiveis, key=lambda r: r["custo_deltas"])
    return min(ativas, key=lambda r: r["custo_deltas"])
