# src/services/resgates.py
"""
Resgates da loja de Deltas.

Camada fina que aplica a transação no usuário em sessão.
"""

from datetime import datetime
from src.data.recompensas import resgatar_recompensa as resgatar_no_catalogo


def efetuar_resgate(usuario, recompensa_id):
    """
    Efetua o resgate: confere saldo, debita Deltas e registra no
    histórico do usuário.
    """
    resultado = resgatar_no_catalogo(recompensa_id, usuario.deltas)

    if resultado["sucesso"]:
        usuario.deltas = resultado["novo_saldo"]
        recompensa = resultado["recompensa"]
        recibo = {
            "id_recibo": f"DELTA-{datetime.now().strftime('%Y%m%d%H%M%S')}-{recompensa_id}",
            "recompensa_id": recompensa_id,
            "nome": recompensa["nome"],
            "custo": recompensa["custo_deltas"],
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "depende_validacao": recompensa["depende_validacao"],
        }
        usuario.recompensas_resgatadas.append(recibo)
        resultado["recibo"] = recibo

    return resultado
