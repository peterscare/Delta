class LearnReel:
    def __init__(self, id, titulo, curso_relacionado, url_video, duracao_segundos):
        self.id = id
        self.titulo = titulo
        self.curso_relacionado = curso_relacionado # Ex: 'Física'[cite: 1]
        self.url_video = url_video
        self.recompensa_visualizacao = 10 # Deltas ganhos por assistir[cite: 1]