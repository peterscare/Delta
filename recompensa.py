# src/models/learn_reel.py


class LearnReel:
    """Representação OO de um Learn Reel (os dados ficam em
    src/data/learn_reels.py como dicts)."""

    def __init__(self, id, titulo, curso, tema_calculo, descricao,
                 interesses=None, duracao_segundos=45, recompensa_deltas=10,
                 url_video=None):
        self.id = id
        self.titulo = titulo
        self.curso = curso
        self.tema_calculo = tema_calculo
        self.descricao = descricao
        self.interesses = interesses or []
        self.duracao_segundos = duracao_segundos
        self.recompensa_deltas = recompensa_deltas
        self.url_video = url_video
