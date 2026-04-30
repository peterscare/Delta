# models/learn_reel.py

class LearnReel:
    """
    Modelo que representa um Learn Reel do Delta.

    Um Learn Reel é um conteúdo curto, estilo reels,
    voltado ao aprendizado rápido de Cálculo I.
    """

    def __init__(
        self,
        id,
        titulo,
        curso,
        tema_calculo,
        interesses,
        descricao,
        url_video=None,
        duracao_segundos=45,
        recompensa_deltas=10,
    ):
        self.id = id
        self.titulo = titulo
        self.curso = curso
        self.tema_calculo = tema_calculo
        self.interesses = interesses
        self.descricao = descricao
        self.url_video = url_video
        self.duracao_segundos = duracao_segundos
        self.recompensa_deltas = recompensa_deltas

    def to_dict(self):
        """
        Converte o Learn Reel para dicionário.
        Útil para exibir no Streamlit ou salvar futuramente.
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "curso": self.curso,
            "tema_calculo": self.tema_calculo,
            "interesses": self.interesses,
            "descricao": self.descricao,
            "url_video": self.url_video,
            "duracao_segundos": self.duracao_segundos,
            "recompensa_deltas": self.recompensa_deltas,
        }