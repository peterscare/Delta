# data/questoes.py

"""
Questões do Delta.

Este arquivo centraliza os exercícios rápidos de Cálculo I.
As questões são usadas para:
- reforçar conceitos básicos;
- gerar engajamento;
- personalizar o conteúdo por curso;
- recompensar o aluno com Deltas ao acertar.

Cada questão possui:
- id: identificador único
- pergunta: enunciado da questão
- curso: curso principal relacionado
- tema_calculo: tema de Cálculo I
- dificuldade: nível da questão
- interesses: interesses que ajudam na personalização
- alternativas: lista de alternativas
- resposta_correta: alternativa correta
- explicacao: explicação exibida após a resposta
- recompensa_deltas: Deltas ganhos ao acertar
"""


QUESTOES = [
    {
        "id": 1,
        "pergunta": "Em Engenharia Mecânica, a derivada da posição em relação ao tempo representa:",
        "curso": "Engenharia Mecânica",
        "tema_calculo": "Derivadas",
        "dificuldade": "Fácil",
        "interesses": ["Esportes", "Ciência", "Tecnologia"],
        "alternativas": [
            "Massa",
            "Velocidade",
            "Temperatura",
            "Pressão",
        ],
        "resposta_correta": "Velocidade",
        "explicacao": (
            "A velocidade instantânea é a derivada da posição em relação ao tempo. "
            "Por isso, derivadas aparecem diretamente em problemas de movimento."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 2,
        "pergunta": "Na Física, a derivada da velocidade em relação ao tempo representa:",
        "curso": "Física",
        "tema_calculo": "Derivadas",
        "dificuldade": "Fácil",
        "interesses": ["Ciência", "Esportes"],
        "alternativas": [
            "Aceleração",
            "Massa",
            "Energia total",
            "Volume",
        ],
        "resposta_correta": "Aceleração",
        "explicacao": (
            "A aceleração é a taxa de variação da velocidade em relação ao tempo, "
            "ou seja, uma derivada."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 3,
        "pergunta": "Em uma rampa, a derivada pode ajudar a interpretar:",
        "curso": "Engenharia Civil",
        "tema_calculo": "Derivadas",
        "dificuldade": "Fácil",
        "interesses": ["Ciência", "Tecnologia"],
        "alternativas": [
            "A inclinação",
            "A cor da rampa",
            "O nome do engenheiro",
            "A marca do cimento",
        ],
        "resposta_correta": "A inclinação",
        "explicacao": (
            "A derivada mede taxa de variação. Em gráficos e modelos, ela pode "
            "representar inclinação."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 4,
        "pergunta": "Em Engenharia de Produção, derivadas podem ser usadas para encontrar:",
        "curso": "Engenharia de Produção",
        "tema_calculo": "Otimização",
        "dificuldade": "Fácil",
        "interesses": ["Finanças", "Empreendedorismo", "Desafios competitivos"],
        "alternativas": [
            "Pontos de máximo e mínimo",
            "A cor de um produto",
            "O nome de uma empresa",
            "A senha de um sistema",
        ],
        "resposta_correta": "Pontos de máximo e mínimo",
        "explicacao": (
            "Derivadas são muito usadas em problemas de otimização, como maximizar "
            "lucros ou minimizar custos."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 5,
        "pergunta": "Um sinal elétrico que varia com o tempo pode ser representado por:",
        "curso": "Engenharia Elétrica",
        "tema_calculo": "Funções",
        "dificuldade": "Fácil",
        "interesses": ["Tecnologia", "Ciência", "Cultura geek"],
        "alternativas": [
            "Uma função",
            "Um parágrafo sem números",
            "Uma cor fixa",
            "Um nome próprio",
        ],
        "resposta_correta": "Uma função",
        "explicacao": (
            "Funções são usadas para representar grandezas que variam, como tensão "
            "ou corrente ao longo do tempo."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 6,
        "pergunta": "Em Ciência da Computação, o crescimento de funções ajuda a analisar:",
        "curso": "Ciência da Computação",
        "tema_calculo": "Funções",
        "dificuldade": "Fácil",
        "interesses": ["Tecnologia", "Jogos", "Cultura geek"],
        "alternativas": [
            "Desempenho de algoritmos",
            "Cor do teclado",
            "Nome do monitor",
            "Tamanho da mochila",
        ],
        "resposta_correta": "Desempenho de algoritmos",
        "explicacao": (
            "A análise de algoritmos usa funções para comparar crescimento de tempo "
            "e uso de memória conforme a entrada aumenta."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 7,
        "pergunta": "Em Engenharia Química, uma taxa de reação pode ser entendida como:",
        "curso": "Engenharia Química",
        "tema_calculo": "Taxas de variação",
        "dificuldade": "Fácil",
        "interesses": ["Ciência", "Tecnologia"],
        "alternativas": [
            "Uma variação ao longo do tempo",
            "Um desenho decorativo",
            "Uma senha de laboratório",
            "Um nome de equipamento",
        ],
        "resposta_correta": "Uma variação ao longo do tempo",
        "explicacao": (
            "Taxas de reação indicam como a concentração de substâncias varia com o tempo, "
            "o que se conecta diretamente com derivadas."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 8,
        "pergunta": "Em Estatística, a área sob uma curva pode estar relacionada a:",
        "curso": "Estatística",
        "tema_calculo": "Integrais",
        "dificuldade": "Fácil",
        "interesses": ["Ciência", "Finanças"],
        "alternativas": [
            "Interpretação de distribuições",
            "Escolha de fonte do texto",
            "Nome de uma tabela",
            "Cor de um gráfico",
        ],
        "resposta_correta": "Interpretação de distribuições",
        "explicacao": (
            "A ideia de área sob uma curva aparece em distribuições, probabilidades "
            "e interpretações estatísticas."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 9,
        "pergunta": "Na Matemática, o conceito de limite é fundamental para definir:",
        "curso": "Matemática",
        "tema_calculo": "Limites",
        "dificuldade": "Fácil",
        "interesses": ["Ciência", "Desafios competitivos"],
        "alternativas": [
            "Derivadas",
            "Ortografia",
            "História antiga",
            "Geografia física",
        ],
        "resposta_correta": "Derivadas",
        "explicacao": (
            "A derivada é definida a partir de um limite. Por isso, limites são uma "
            "das bases do Cálculo I."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 10,
        "pergunta": "Em jogos, uma função pode representar:",
        "curso": "Outro curso de exatas",
        "tema_calculo": "Funções",
        "dificuldade": "Fácil",
        "interesses": ["Jogos", "Cultura geek"],
        "alternativas": [
            "Vida do personagem ao longo do tempo",
            "Apenas o nome do jogo",
            "A cor do controle",
            "O formato da cadeira",
        ],
        "resposta_correta": "Vida do personagem ao longo do tempo",
        "explicacao": (
            "Funções podem representar grandezas que mudam, como vida, dano, pontuação "
            "ou evolução de um personagem."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 11,
        "pergunta": "Em esportes, a velocidade instantânea de um atleta está ligada a qual conceito?",
        "curso": "Outro curso de exatas",
        "tema_calculo": "Derivadas",
        "dificuldade": "Fácil",
        "interesses": ["Esportes", "Desafios competitivos"],
        "alternativas": [
            "Derivada",
            "Substantivo",
            "Pontuação final",
            "Uniforme",
        ],
        "resposta_correta": "Derivada",
        "explicacao": (
            "A velocidade instantânea pode ser interpretada como a derivada da posição "
            "em relação ao tempo."
        ),
        "recompensa_deltas": 20,
    },
    {
        "id": 12,
        "pergunta": "Uma função contínua, de forma intuitiva, é aquela cujo gráfico:",
        "curso": "Matemática",
        "tema_calculo": "Continuidade",
        "dificuldade": "Fácil",
        "interesses": ["Ciência", "Desafios competitivos"],
        "alternativas": [
            "Não apresenta quebras bruscas",
            "Sempre é uma reta",
            "Nunca usa números",
            "Só existe em computadores",
        ],
        "resposta_correta": "Não apresenta quebras bruscas",
        "explicacao": (
            "De forma intuitiva, continuidade significa que o gráfico não tem saltos, "
            "buracos ou quebras naquele ponto ou intervalo."
        ),
        "recompensa_deltas": 20,
    },
]


def listar_questoes():
    """
    Retorna todas as questões cadastradas.
    """
    return QUESTOES


def buscar_questao_por_id(questao_id):
    """
    Busca uma questão pelo ID.
    Retorna a questão encontrada ou None.
    """
    for questao in QUESTOES:
        if questao["id"] == questao_id:
            return questao
    return None


def listar_questoes_por_curso(nome_curso):
    """
    Retorna questões relacionadas diretamente ao curso do aluno.
    Também inclui questões gerais de 'Outro curso de exatas'.
    """
    return [
        questao
        for questao in QUESTOES
        if questao["curso"] == nome_curso or questao["curso"] == "Outro curso de exatas"
    ]


def listar_questoes_por_interesse(interesses_usuario):
    """
    Retorna questões que combinam com pelo menos um interesse do usuário.

    interesses_usuario deve ser uma lista de strings.
    Exemplo:
    ['Tecnologia', 'Jogos']
    """
    questoes_recomendadas = []

    for questao in QUESTOES:
        for interesse in interesses_usuario:
            if interesse in questao["interesses"]:
                questoes_recomendadas.append(questao)
                break

    return questoes_recomendadas


def listar_questoes_por_tema(tema_calculo):
    """
    Retorna questões de um tema específico de Cálculo I.
    """
    return [
        questao
        for questao in QUESTOES
        if questao["tema_calculo"] == tema_calculo
    ]


def listar_questoes_por_dificuldade(dificuldade):
    """
    Retorna questões de uma dificuldade específica.
    Exemplo: 'Fácil'
    """
    return [
        questao
        for questao in QUESTOES
        if questao["dificuldade"] == dificuldade
    ]


def recomendar_questoes(nome_curso, interesses_usuario, limite=5):
    """
    Recomenda questões combinando curso e interesses do usuário.

    A prioridade é:
    1. Questões do curso do aluno
    2. Questões ligadas aos interesses declarados
    3. Questões gerais
    """
    recomendadas = []
    ids_adicionados = set()

    # 1. Prioriza questões do curso
    for questao in listar_questoes_por_curso(nome_curso):
        recomendadas.append(questao)
        ids_adicionados.add(questao["id"])

    # 2. Adiciona questões por interesse sem duplicar
    for questao in listar_questoes_por_interesse(interesses_usuario):
        if questao["id"] not in ids_adicionados:
            recomendadas.append(questao)
            ids_adicionados.add(questao["id"])

    # 3. Completa com questões gerais se necessário
    for questao in QUESTOES:
        if questao["curso"] == "Outro curso de exatas" and questao["id"] not in ids_adicionados:
            recomendadas.append(questao)
            ids_adicionados.add(questao["id"])

    return recomendadas[:limite]


def verificar_resposta(questao_id, resposta_usuario):
    """
    Verifica se a resposta do usuário está correta.

    Retorna True se estiver correta.
    Retorna False se estiver errada ou se a questão não existir.
    """
    questao = buscar_questao_por_id(questao_id)

    if questao is None:
        return False

    return resposta_usuario == questao["resposta_correta"]


def obter_explicacao(questao_id):
    """
    Retorna a explicação de uma questão.
    """
    questao = buscar_questao_por_id(questao_id)

    if questao is None:
        return ""

    return questao["explicacao"]


def calcular_deltas_questao(questao_id, resposta_usuario):
    """
    Calcula os Deltas ganhos ao responder uma questão.

    Se acertar, retorna a recompensa da questão.
    Se errar, retorna 0.
    """
    questao = buscar_questao_por_id(questao_id)

    if questao is None:
        return 0

    if verificar_resposta(questao_id, resposta_usuario):
        return questao["recompensa_deltas"]

    return 0