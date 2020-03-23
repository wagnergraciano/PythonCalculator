from jogador import Jogador

class Goleiro(Jogador):
    def __init__(self,golsSofridos):
        super().__init__(camisa,posicao,gols)
        self.golsSofridos = golsSofridos