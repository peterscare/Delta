# data/recompensas.py

"""
Recompensas do Delta.

Este arquivo centraliza as recompensas que podem ser resgatadas com Deltas.

As recompensas foram pensadas para o contexto do Hackathon e podem ser:
- simbólicas;
- acadêmicas;
- institucionais;
- dependentes de parceria com a Escola Politécnica da UFRJ.

Cada recompensa possui:
- id: identificador único
- nome: nome da recompensa
- descricao: explicação da recompensa
- custo_deltas: quantidade de Deltas necessária para resgatar
- tipo: categoria da recompensa
- parceiro: responsável ou parceiro envolvido
- ativa: indica se a recompensa está disponível
- depende_validacao: indica se depende de validação institucional
"""


RECOMPENSAS = [
    {
        "id": 1,
        "nome": "Certificado de participação",
        "descricao": (
            "Certificado simbólico para alunos que participarem ativamente "
            "da plataforma Delta."
        ),
        "custo_deltas": 100,
        "tipo": "Acadêmica",
        "parceiro": "Projeto Delta",
        "ativa": True,
        "depende_validacao": False,
    },
    {
        "id": 2,
        "nome": "Badge de destaque acadêmico",
        "descricao": (
            "Selo digital para estudantes que mantiverem bom desempenho "
            "e constância no uso do aplicativo."
        ),
        "custo_deltas": 150,
        "tipo": "Gamificação",
        "parceiro": "Projeto Delta",
        "ativa": True,
        "depende_validacao": False,
    },
    {
        "id": 3,
        "nome": "Participação em sorteio de benefício",
        "descricao": (
            "Entrada simbólica em sorteio de benefício institucional, "
            "dependente de regras e validação da universidade."
        ),
        "custo_deltas": 300,
        "tipo": "Institucional",
        "parceiro": "Escola Politécnica da UFRJ",
        "ativa": True,
        "depende_validacao": True,
    },
    {
        "id": 4,
        "nome": "Benefício institucional via parceria",
        "descricao": (
            "Recompensa viabilizada por parceria com a Escola Politécnica da UFRJ, "
            "podendo envolver auxílios, créditos simbólicos ou outros incentivos."
        ),
        "custo_deltas": 500,
        "tipo": "Institucional",
        "parceiro": "Escola Politécnica da UFRJ",
        "ativa": True,
        "depende_validacao": True,
    },
    {
        "id": 5,
        "nome": "Prioridade simbólica em atividade acadêmica",
        "descricao": (
            "Benefício simbólico que poderia oferecer prioridade em inscrições "
            "de oficinas, minicursos ou atividades ligadas ao projeto."
        ),
        "custo_deltas": 250,
        "tipo": "Acadêmica",
        "parceiro": "Coordenação do Projeto",
        "ativa": True,
        "depende_validacao": True,
    },
    {
        "id": 6,
        "nome": "Cupom Delta",
        "descricao": (
            "Cupom simbólico de engajamento que pode ser usado futuramente "
            "em ações patrocinadas ou parcerias do projeto."
        ),
        "custo_deltas": 200,
        "tipo": "Parceria",
        "parceiro": "Parceiros externos ou institucionais",
        "ativa": True,
        "depende_validacao": True,
    },
    {
        "id": 7,
        "nome": "Título de Top Delta da semana",
        "descricao": (
            "Reconhecimento semanal para alunos que ficarem entre os primeiros "
            "do ranking."
        ),
        "custo_deltas": 0,
        "tipo": "Ranking",
        "parceiro": "Projeto Delta",
        "ativa": True,
        "depende_validacao": False,
    },
    {
        "id": 8,
        "nome": "Desafio bônus liberado",
        "descricao": (
            "Liberação de desafios extras que oferecem mais Deltas e aumentam "
            "a competitividade entre os estudantes."
        ),
        "custo_deltas": 80,
        "tipo": "Gamificação",
        "parceiro": "Projeto Delta",
        "ativa": True,
        "depende_validacao": False,
    },
]


def listar_recompensas():
    """
    Retorna todas as recompensas cadastradas.
    """
    return RECOMPENSAS


def listar_recompensas_ativas():
    """
    Retorna apenas recompensas disponíveis para resgate.
    """
    return [
        recompensa
        for recompensa in RECOMPENSAS
        if recompensa["ativa"] is True
    ]


def buscar_recompensa_por_id(recompensa_id):
    """
    Busca uma recompensa pelo ID.
    Retorna a recompensa encontrada ou None.
    """
    for recompensa in RECOMPENSAS:
        if recompensa["id"] == recompensa_id:
            return recompensa
    return None


def listar_recompensas_por_tipo(tipo):
    """
    Retorna recompensas de uma categoria específica.

    Exemplos de tipo:
    - 'Acadêmica'
    - 'Gamificação'
    - 'Institucional'
    - 'Parceria'
    - 'Ranking'
    """
    return [
        recompensa
        for recompensa in RECOMPENSAS
        if recompensa["tipo"] == tipo
    ]


def listar_recompensas_por_custo_maximo(saldo_deltas):
    """
    Retorna recompensas que o aluno consegue resgatar
    com o saldo atual de Deltas.
    """
    return [
        recompensa
        for recompensa in RECOMPENSAS
        if recompensa["ativa"] is True
        and recompensa["custo_deltas"] <= saldo_deltas
    ]


def verificar_se_pode_resgatar(recompensa_id, saldo_deltas):
    """
    Verifica se o aluno possui Deltas suficientes para resgatar a recompensa.

    Retorna True se puder resgatar.
    Retorna False caso contrário.
    """
    recompensa = buscar_recompensa_por_id(recompensa_id)

    if recompensa is None:
        return False

    if recompensa["ativa"] is False:
        return False

    return saldo_deltas >= recompensa["custo_deltas"]


def resgatar_recompensa(recompensa_id, saldo_deltas):
    """
    Tenta resgatar uma recompensa.

    Retorna um dicionário com:
    - sucesso: True ou False
    - mensagem: texto explicando o resultado
    - novo_saldo: saldo atualizado
    - recompensa: recompensa resgatada ou None
    """
    recompensa = buscar_recompensa_por_id(recompensa_id)

    if recompensa is None:
        return {
            "sucesso": False,
            "mensagem": "Recompensa não encontrada.",
            "novo_saldo": saldo_deltas,
            "recompensa": None,
        }

    if recompensa["ativa"] is False:
        return {
            "sucesso": False,
            "mensagem": "Esta recompensa não está disponível no momento.",
            "novo_saldo": saldo_deltas,
            "recompensa": recompensa,
        }

    if saldo_deltas < recompensa["custo_deltas"]:
        return {
            "sucesso": False,
            "mensagem": "Saldo de Deltas insuficiente para resgatar esta recompensa.",
            "novo_saldo": saldo_deltas,
            "recompensa": recompensa,
        }

    novo_saldo = saldo_deltas - recompensa["custo_deltas"]

    mensagem = "Recompensa resgatada com sucesso."

    if recompensa["depende_validacao"]:
        mensagem += " Esta recompensa depende de validação institucional."

    return {
        "sucesso": True,
        "mensagem": mensagem,
        "novo_saldo": novo_saldo,
        "recompensa": recompensa,
    }


def obter_recompensa_em_destaque(saldo_deltas):
    """
    Retorna uma recompensa para aparecer em destaque na Home.

    Estratégia:
    - Se o aluno já consegue resgatar algo, mostra a melhor recompensa disponível.
    - Se não consegue, mostra a recompensa ativa mais barata.
    """
    recompensas_ativas = listar_recompensas_ativas()

    if not recompensas_ativas:
        return None

    recompensas_disponiveis = listar_recompensas_por_custo_maximo(saldo_deltas)

    if recompensas_disponiveis:
        return max(
            recompensas_disponiveis,
            key=lambda recompensa: recompensa["custo_deltas"]
        )

    return min(
        recompensas_ativas,
        key=lambda recompensa: recompensa["custo_deltas"]
    )