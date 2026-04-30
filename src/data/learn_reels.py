# src/data/learn_reels.py
"""
Learn Reels do Delta.

Conteúdos curtos (estilo reels) voltados ao aprendizado de Cálculo I,
com personalização por curso e por interesses do aluno.
"""


LEARN_REELS = [
    {
        "id": 1,
        "titulo": "Derivada como velocidade instantânea",
        "curso": "Engenharia Mecânica",
        "tema_calculo": "Derivadas",
        "interesses": ["Esportes", "Jogos", "Ciência"],
        "descricao": "Mostra como a derivada da posição em relação ao tempo representa a velocidade instantânea de um objeto em movimento.",
        "duracao_segundos": 45,
        "recompensa_deltas": 10,
    },
    {
        "id": 2,
        "titulo": "Aceleração e segunda derivada",
        "curso": "Engenharia Mecânica",
        "tema_calculo": "Derivadas",
        "interesses": ["Esportes", "Ciência", "Tecnologia"],
        "descricao": "Explica como a segunda derivada da posição pode representar a aceleração de um corpo.",
        "duracao_segundos": 50,
        "recompensa_deltas": 10,
    },
    {
        "id": 3,
        "titulo": "Derivadas e inclinação em estruturas",
        "curso": "Engenharia Civil",
        "tema_calculo": "Derivadas",
        "interesses": ["Ciência", "Tecnologia"],
        "descricao": "Relaciona derivadas com inclinação de rampas, curvas e estruturas presentes em projetos de Engenharia Civil.",
        "duracao_segundos": 50,
        "recompensa_deltas": 10,
    },
    {
        "id": 4,
        "titulo": "Integrais e cálculo de áreas",
        "curso": "Engenharia Civil",
        "tema_calculo": "Integrais",
        "interesses": ["Ciência", "Empreendedorismo"],
        "descricao": "Apresenta a ideia de integral como ferramenta para calcular áreas aproximadas em projetos e construções.",
        "duracao_segundos": 55,
        "recompensa_deltas": 10,
    },
    {
        "id": 5,
        "titulo": "Funções em sinais elétricos",
        "curso": "Engenharia Elétrica",
        "tema_calculo": "Funções",
        "interesses": ["Tecnologia", "Ciência", "Cultura geek"],
        "descricao": "Mostra como sinais elétricos podem ser representados por funções que variam ao longo do tempo.",
        "duracao_segundos": 45,
        "recompensa_deltas": 10,
    },
    {
        "id": 6,
        "titulo": "Limites em circuitos",
        "curso": "Engenharia Elétrica",
        "tema_calculo": "Limites",
        "interesses": ["Tecnologia", "Ciência"],
        "descricao": "Explica como limites podem ajudar a entender o comportamento de grandezas elétricas em situações extremas.",
        "duracao_segundos": 50,
        "recompensa_deltas": 10,
    },
    {
        "id": 7,
        "titulo": "Derivadas para otimizar custos",
        "curso": "Engenharia de Produção",
        "tema_calculo": "Otimização",
        "interesses": ["Finanças", "Empreendedorismo", "Desafios competitivos"],
        "descricao": "Mostra como derivadas podem ajudar a encontrar pontos de máximo e mínimo em problemas de custo, lucro e produtividade.",
        "duracao_segundos": 55,
        "recompensa_deltas": 10,
    },
    {
        "id": 8,
        "titulo": "Funções de produtividade",
        "curso": "Engenharia de Produção",
        "tema_calculo": "Funções",
        "interesses": ["Finanças", "Empreendedorismo"],
        "descricao": "Explica como funções podem representar produção, custo, lucro e eficiência em processos.",
        "duracao_segundos": 45,
        "recompensa_deltas": 10,
    },
    {
        "id": 9,
        "titulo": "Taxas de reação em Engenharia Química",
        "curso": "Engenharia Química",
        "tema_calculo": "Taxas de variação",
        "interesses": ["Ciência", "Tecnologia"],
        "descricao": "Relaciona taxas de variação com a velocidade de reações químicas e mudanças de concentração.",
        "duracao_segundos": 50,
        "recompensa_deltas": 10,
    },
    {
        "id": 10,
        "titulo": "Funções em processos químicos",
        "curso": "Engenharia Química",
        "tema_calculo": "Funções",
        "interesses": ["Ciência", "Tecnologia"],
        "descricao": "Mostra como funções podem modelar temperatura, pressão, concentração e outras variáveis em processos químicos.",
        "duracao_segundos": 50,
        "recompensa_deltas": 10,
    },
    {
        "id": 11,
        "titulo": "Crescimento de funções e algoritmos",
        "curso": "Ciência da Computação",
        "tema_calculo": "Funções",
        "interesses": ["Tecnologia", "Jogos", "Cultura geek"],
        "descricao": "Conecta o crescimento de funções com análise de desempenho de algoritmos e uso de recursos computacionais.",
        "duracao_segundos": 45,
        "recompensa_deltas": 10,
    },
    {
        "id": 12,
        "titulo": "Limites e comportamento assintótico",
        "curso": "Ciência da Computação",
        "tema_calculo": "Limites",
        "interesses": ["Tecnologia", "Cultura geek"],
        "descricao": "Mostra como limites ajudam a entender o comportamento de funções quando as entradas ficam muito grandes.",
        "duracao_segundos": 50,
        "recompensa_deltas": 10,
    },
    {
        "id": 13,
        "titulo": "Cálculo e movimento",
        "curso": "Física",
        "tema_calculo": "Derivadas",
        "interesses": ["Ciência", "Esportes", "Tecnologia"],
        "descricao": "Explica como velocidade e aceleração são descritas usando derivadas em problemas de movimento.",
        "duracao_segundos": 45,
        "recompensa_deltas": 10,
    },
    {
        "id": 14,
        "titulo": "Integrais e deslocamento",
        "curso": "Física",
        "tema_calculo": "Integrais",
        "interesses": ["Ciência", "Tecnologia"],
        "descricao": "Mostra como integrais podem representar deslocamento a partir de uma função velocidade.",
        "duracao_segundos": 55,
        "recompensa_deltas": 10,
    },
    {
        "id": 15,
        "titulo": "Limites: a base do Cálculo",
        "curso": "Matemática",
        "tema_calculo": "Limites",
        "interesses": ["Ciência", "Desafios competitivos"],
        "descricao": "Apresenta limites como uma das ideias centrais para entender derivadas, continuidade e integrais.",
        "duracao_segundos": 50,
        "recompensa_deltas": 10,
    },
    {
        "id": 16,
        "titulo": "Continuidade sem mistério",
        "curso": "Matemática",
        "tema_calculo": "Continuidade",
        "interesses": ["Ciência", "Desafios competitivos"],
        "descricao": "Explica de forma simples o que significa uma função ser contínua e por que isso importa em Cálculo I.",
        "duracao_segundos": 45,
        "recompensa_deltas": 10,
    },
    {
        "id": 17,
        "titulo": "Funções e modelos de dados",
        "curso": "Estatística",
        "tema_calculo": "Funções",
        "interesses": ["Ciência", "Tecnologia", "Finanças"],
        "descricao": "Mostra como funções ajudam a representar tendências, padrões e variações em conjuntos de dados.",
        "duracao_segundos": 45,
        "recompensa_deltas": 10,
    },
    {
        "id": 18,
        "titulo": "Área sob a curva",
        "curso": "Estatística",
        "tema_calculo": "Integrais",
        "interesses": ["Ciência", "Finanças"],
        "descricao": "Introduz a ideia de área sob uma curva e sua relação com interpretação de dados e distribuições.",
        "duracao_segundos": 55,
        "recompensa_deltas": 10,
    },
    {
        "id": 19,
        "titulo": "Cálculo em jogos: vida, dano e evolução",
        "curso": "Outro curso de exatas",
        "tema_calculo": "Funções",
        "interesses": ["Jogos", "Cultura geek"],
        "descricao": "Usa exemplos de jogos para mostrar como funções podem representar vida do personagem, dano, níveis e progressão.",
        "duracao_segundos": 40,
        "recompensa_deltas": 10,
    },
    {
        "id": 20,
        "titulo": "Derivadas em esportes",
        "curso": "Outro curso de exatas",
        "tema_calculo": "Derivadas",
        "interesses": ["Esportes", "Desafios competitivos"],
        "descricao": "Mostra como derivadas aparecem em velocidade, aceleração, arrancadas e desempenho esportivo.",
        "duracao_segundos": 40,
        "recompensa_deltas": 10,
    },
]


def listar_learn_reels():
    return LEARN_REELS


def buscar_learn_reel_por_id(reel_id):
    for reel in LEARN_REELS:
        if reel["id"] == reel_id:
            return reel
    return None


def listar_learn_reels_por_curso(nome_curso):
    return [
        reel
        for reel in LEARN_REELS
        if reel["curso"] == nome_curso or reel["curso"] == "Outro curso de exatas"
    ]


def listar_learn_reels_por_interesse(interesses_usuario):
    if not interesses_usuario:
        return []
    recomendados = []
    for reel in LEARN_REELS:
        for interesse in interesses_usuario:
            if interesse in reel["interesses"]:
                recomendados.append(reel)
                break
    return recomendados


def recomendar_learn_reels(nome_curso, interesses_usuario, limite=10):
    """Combina curso + interesses, sem duplicar, com fallback geral."""
    recomendados = []
    ids = set()

    for reel in listar_learn_reels_por_curso(nome_curso):
        if reel["id"] not in ids:
            recomendados.append(reel)
            ids.add(reel["id"])

    for reel in listar_learn_reels_por_interesse(interesses_usuario or []):
        if reel["id"] not in ids:
            recomendados.append(reel)
            ids.add(reel["id"])

    for reel in LEARN_REELS:
        if reel["curso"] == "Outro curso de exatas" and reel["id"] not in ids:
            recomendados.append(reel)
            ids.add(reel["id"])

    return recomendados[:limite]


def calcular_deltas_learn_reel(reel_id):
    reel = buscar_learn_reel_por_id(reel_id)
    return 0 if reel is None else reel["recompensa_deltas"]
