# Lista oficial de cursos que utilizam Cálculo I na UFRJ para o Projeto Delta

LISTA_CURSOS = [
    # Engenharias (Poli e Escola de Química)
    "Engenharia Civil",
    "Engenharia Mecânica",
    "Engenharia Elétrica",
    "Engenharia Eletrônica e de Computação",
    "Engenharia de Controle e Automação",
    "Engenharia de Produção",
    "Engenharia Naval e Oceânica",
    "Engenharia Nuclear",
    "Engenharia Metalúrgica",
    "Engenharia de Materiais",
    "Engenharia de Petróleo",
    "Engenharia Química",
    "Engenharia de Alimentos",
    "Engenharia Ambiental",
    
    # Ciências Exatas (CCMN)
    "Matemática",
    "Física",
    "Astronomia",
    "Ciência da Computação",
    "Estatística",
    "Geologia",
    "Meteorologia",
    "Química",
    "Nanotecnologia",
    "BCMT (Bacharelado em Ciências Matemáticas e da Natureza)",
    
    # Outros
    "Arquitetura e Urbanismo",
    "Economia",
    "Ciências Atuariais"
]

# Função auxiliar para o Front-end usar no st.selectbox
def obter_nomes_cursos():
    return sorted(LISTA_CURSOS)