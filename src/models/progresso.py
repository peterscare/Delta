from datetime import datetime

class Progresso:
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id
        self.atividades_concluidas = [] # Lista de IDs de exercícios/reels
        self.data_ultimo_acesso = datetime.now()
        self.total_deltas_acumulados = 0 # Histórico total, independente do saldo atual