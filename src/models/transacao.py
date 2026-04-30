from datetime import datetime

class Transacao:
    def __init__(self, usuario_id, recompensa_id, valor_pago):
        # Gera um código de recibo para o aluno apresentar na Escola Politécnica se necessário
        self.id_recibo = f"DELTA-{datetime.now().strftime('%Y%m%d')}-{usuario_id[:4]}"
        self.usuario_id = usuario_id
        self.recompensa_id = recompensa_id
        self.valor_pago = valor_pago
        self.data_resgate = datetime.now()