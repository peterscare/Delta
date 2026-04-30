# src/data/exercicios.py
"""
Exercícios (questões rápidas) do Delta.

Reforçam conceitos de Cálculo I, geram engajamento, personalizam o
conteúdo por curso e por interesses e recompensam o aluno em Deltas
quando ele acerta.
"""


EXERCICIOS = [
    {
        "id": 1,
        "pergunta": "Em Engenharia Mecânica, a derivada da posição em relação ao tempo representa:",
        "curso": "Engenharia Mecânica",
        "tema_calculo": "Derivadas",
        "dificuldade": "Fácil",
        "interesses": ["Esportes", "Ciência", "Tecnologia"],
        "alternativas": ["Massa", "Velocidade", "Temperatura", "Pressão"],
        "resposta_correta": "Velocidade",
        "explicacao": "A velocidade instantânea é a derivada da posição em relação ao tempo. Por isso, derivadas aparecem diretamente em problemas de movimento.",
        "recompensa_deltas": 20,
    },
    {
        "id": 2,
        "pergunta": "Na Física, a derivada da velocidade em relação ao tempo representa:",
        "curso": "Física",
        "tema_calculo": "Derivadas",
        "dificuldade": "Fácil",
        "interesses": ["Ciência", "Esportes"],
        "alternativas": ["Aceleração", "Massa", "Energia total", "Volume"],
        "resposta_correta": "Aceleração",
        "explicacao": "A aceleração é a taxa de variação da velocidade em relação ao tempo, ou seja, uma derivada.",
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
        "explicacao": "A derivada mede taxa de variação. Em gráficos e modelos, ela pode representar inclinação.",
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
        "explicacao": "Derivadas são muito usadas em problemas de otimização, como maximizar lucros ou minimizar custos.",
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
        "explicacao": "Funções são usadas para representar grandezas que variam, como tensão ou corrente ao longo do tempo.",
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
        "explicacao": "A análise de algoritmos usa funções para comparar crescimento de tempo e uso de memória conforme a entrada aumenta.",
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
        "explicacao": "Taxas de reação indicam como a concentração de substâncias varia com o tempo, o que se conecta diretamente com derivadas.",
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
        "explicacao": "A ideia de área sob uma curva aparece em distribuições, probabilidades e interpretações estatísticas.",
        "recompensa_deltas": 20,
    },
    {
        "id": 9,
        "pergunta": "Na Matemática, o conceito de limite é fundamental para definir:",
        "curso": "Matemática",
        "tema_calculo": "Limites",
        "dificuldade": "Fácil",
        "interesses": ["Ciência", "Desafios competitivos"],
        "alternativas": ["Derivadas", "Ortografia", "História antiga", "Geografia física"],
        "resposta_correta": "Derivadas",
        "explicacao": "A derivada é definida a partir de um limite. Por isso, limites são uma das bases do Cálculo I.",
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
        "explicacao": "Funções podem representar grandezas que mudam, como vida, dano, pontuação ou evolução de um personagem.",
        "recompensa_deltas": 20,
    },
    {
        "id": 11,
        "pergunta": "Em esportes, a velocidade instantânea de um atleta está ligada a qual conceito?",
        "curso": "Outro curso de exatas",
        "tema_calculo": "Derivadas",
        "dificuldade": "Fácil",
        "interesses": ["Esportes", "Desafios competitivos"],
        "alternativas": ["Derivada", "Substantivo", "Pontuação final", "Uniforme"],
        "resposta_correta": "Derivada",
        "explicacao": "A velocidade instantânea pode ser interpretada como a derivada da posição em relação ao tempo.",
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
        "explicacao": "De forma intuitiva, continuidade significa que o gráfico não tem saltos, buracos ou quebras naquele ponto ou intervalo.",
        "recompensa_deltas": 20,
    },
    {
        "id": 13,
        "pergunta": "O limite de f(x) = (x² - 1) / (x - 1) quando x tende a 1 vale:",
        "curso": "Matemática",
        "tema_calculo": "Limites",
        "dificuldade": "Médio",
        "interesses": ["Ciência", "Desafios competitivos"],
        "alternativas": ["0", "1", "2", "Não existe"],
        "resposta_correta": "2",
        "explicacao": "Fatorando o numerador como (x-1)(x+1), simplificamos com (x-1) e o limite vira x+1 → 1+1 = 2.",
        "recompensa_deltas": 30,
    },
    {
        "id": 14,
        "pergunta": "A derivada de f(x) = x³ é:",
        "curso": "Matemática",
        "tema_calculo": "Derivadas",
        "dificuldade": "Fácil",
        "interesses": ["Ciência"],
        "alternativas": ["x²", "3x²", "3x", "x³/3"],
        "resposta_correta": "3x²",
        "explicacao": "Pela regra da potência, d/dx (xⁿ) = n·xⁿ⁻¹. Para n=3, obtemos 3x².",
        "recompensa_deltas": 20,
    },
    {
        "id": 15,
        "pergunta": "A integral indefinida de f(x) = 2x é:",
        "curso": "Matemática",
        "tema_calculo": "Integrais",
        "dificuldade": "Fácil",
        "interesses": ["Ciência"],
        "alternativas": ["x² + C", "2 + C", "x + C", "2x² + C"],
        "resposta_correta": "x² + C",
        "explicacao": "A primitiva de 2x é x² (mais constante), pois a derivada de x² é 2x.",
        "recompensa_deltas": 20,
    },
]


def listar_exercicios():
    return EXERCICIOS


def buscar_exercicio_por_id(exercicio_id):
    for ex in EXERCICIOS:
        if ex["id"] == exercicio_id:
            return ex
    return None


def listar_exercicios_por_curso(nome_curso):
    return [
        ex
        for ex in EXERCICIOS
        if ex["curso"] == nome_curso or ex["curso"] == "Outro curso de exatas"
    ]


def listar_exercicios_por_interesse(interesses_usuario):
    if not interesses_usuario:
        return []
    recomendados = []
    for ex in EXERCICIOS:
        for interesse in interesses_usuario:
            if interesse in ex["interesses"]:
                recomendados.append(ex)
                break
    return recomendados


def listar_exercicios_por_tema(tema_calculo):
    return [ex for ex in EXERCICIOS if ex["tema_calculo"] == tema_calculo]


def recomendar_exercicios(nome_curso, interesses_usuario=None, limite=10):
    interesses_usuario = interesses_usuario or []
    recomendados = []
    ids = set()

    for ex in listar_exercicios_por_curso(nome_curso):
        if ex["id"] not in ids:
            recomendados.append(ex)
            ids.add(ex["id"])

    for ex in listar_exercicios_por_interesse(interesses_usuario):
        if ex["id"] not in ids:
            recomendados.append(ex)
            ids.add(ex["id"])

    for ex in EXERCICIOS:
        if ex["curso"] == "Outro curso de exatas" and ex["id"] not in ids:
            recomendados.append(ex)
            ids.add(ex["id"])

    return recomendados[:limite]


def verificar_resposta(exercicio_id, resposta_usuario):
    ex = buscar_exercicio_por_id(exercicio_id)
    if ex is None:
        return False
    return resposta_usuario == ex["resposta_correta"]


def calcular_deltas_exercicio(exercicio_id, resposta_usuario):
    ex = buscar_exercicio_por_id(exercicio_id)
    if ex is None:
        return 0
    if verificar_resposta(exercicio_id, resposta_usuario):
        return ex["recompensa_deltas"]
    return 0
