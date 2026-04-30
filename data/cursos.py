# data/cursos.py

"""
Cursos disponíveis no Delta.

Este arquivo centraliza os cursos que aparecem no cadastro do aluno.
Cada curso possui:
- id: identificador único
- nome: nome exibido no app
- area: área geral do curso
- descricao: breve explicação
- temas_calculo: temas de Cálculo I que combinam com o curso
"""


CURSOS = [
    {
        "id": 1,
        "nome": "Engenharia Civil",
        "area": "Engenharia",
        "descricao": "Curso ligado a estruturas, construção, infraestrutura, materiais e projetos.",
        "temas_calculo": [
            "Derivadas e inclinação",
            "Integrais e cálculo de áreas",
            "Otimização de estruturas",
            "Taxas de variação",
        ],
    },
    {
        "id": 2,
        "nome": "Engenharia Mecânica",
        "area": "Engenharia",
        "descricao": "Curso ligado a máquinas, movimento, energia, forças e sistemas mecânicos.",
        "temas_calculo": [
            "Derivada como velocidade",
            "Segunda derivada como aceleração",
            "Movimento de partículas",
            "Otimização mecânica",
        ],
    },
    {
        "id": 3,
        "nome": "Engenharia Elétrica",
        "area": "Engenharia",
        "descricao": "Curso ligado a circuitos, sinais elétricos, energia, eletrônica e sistemas de potência.",
        "temas_calculo": [
            "Funções em sinais elétricos",
            "Limites em circuitos",
            "Taxas de variação de corrente",
            "Modelagem de sinais",
        ],
    },
    {
        "id": 4,
        "nome": "Engenharia de Produção",
        "area": "Engenharia",
        "descricao": "Curso ligado a processos, produtividade, custos, logística, gestão e otimização.",
        "temas_calculo": [
            "Derivadas para otimização",
            "Máximos e mínimos",
            "Funções de custo",
            "Modelagem de produtividade",
        ],
    },
    {
        "id": 5,
        "nome": "Engenharia Química",
        "area": "Engenharia",
        "descricao": "Curso ligado a processos químicos, reações, produção industrial e transformação de materiais.",
        "temas_calculo": [
            "Taxas de reação",
            "Variação de concentração",
            "Funções em processos químicos",
            "Modelagem de sistemas",
        ],
    },
    {
        "id": 6,
        "nome": "Ciência da Computação",
        "area": "Exatas",
        "descricao": "Curso ligado a algoritmos, programação, dados, sistemas e inteligência computacional.",
        "temas_calculo": [
            "Crescimento de funções",
            "Limites e comportamento assintótico",
            "Funções em algoritmos",
            "Otimização computacional",
        ],
    },
    {
        "id": 7,
        "nome": "Matemática",
        "area": "Exatas",
        "descricao": "Curso ligado à teoria matemática, funções, demonstrações, estruturas e abstrações.",
        "temas_calculo": [
            "Limites",
            "Derivadas",
            "Integrais",
            "Continuidade",
        ],
    },
    {
        "id": 8,
        "nome": "Física",
        "area": "Exatas",
        "descricao": "Curso ligado a movimento, forças, energia, fenômenos naturais e modelagem matemática.",
        "temas_calculo": [
            "Derivada como velocidade",
            "Segunda derivada como aceleração",
            "Integrais em movimento",
            "Modelagem física",
        ],
    },
    {
        "id": 9,
        "nome": "Estatística",
        "area": "Exatas",
        "descricao": "Curso ligado a dados, probabilidade, modelos, análise estatística e tomada de decisão.",
        "temas_calculo": [
            "Funções em modelos de dados",
            "Taxas de variação",
            "Áreas sob curvas",
            "Modelagem matemática",
        ],
    },
    {
        "id": 10,
        "nome": "Outro curso de exatas",
        "area": "Exatas",
        "descricao": "Categoria geral para alunos de cursos de exatas não listados diretamente.",
        "temas_calculo": [
            "Limites",
            "Derivadas",
            "Integrais",
            "Aplicações gerais de Cálculo I",
        ],
    },
]


def listar_cursos():
    """
    Retorna a lista completa de cursos.
    """
    return CURSOS


def listar_nomes_cursos():
    """
    Retorna apenas os nomes dos cursos.
    Útil para usar em selectbox no Streamlit.
    """
    return [curso["nome"] for curso in CURSOS]


def buscar_curso_por_id(curso_id):
    """
    Busca um curso pelo ID.
    Retorna o curso encontrado ou None.
    """
    for curso in CURSOS:
        if curso["id"] == curso_id:
            return curso
    return None


def buscar_curso_por_nome(nome_curso):
    """
    Busca um curso pelo nome.
    Retorna o curso encontrado ou None.
    """
    for curso in CURSOS:
        if curso["nome"] == nome_curso:
            return curso
    return None


def obter_temas_por_curso(nome_curso):
    """
    Retorna os temas de Cálculo I associados a um curso.
    """
    curso = buscar_curso_por_nome(nome_curso)

    if curso is None:
        return []

    return curso["temas_calculo"]
