from .jogador import Jogador

class Time():
    def __init__(self,nome,jogadores,vitoria,derrota,empate):
        self.nome = nome
        # if isinstance(jogadores,Jogador) verificar se instancias na lista sao jogadores
        self.jogadores = jogadores
        self.vitoria = vitoria
        self.derrota = derrota
        self.empare = empate

# implementar classes