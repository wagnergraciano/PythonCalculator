from .jogador import Jogador

class Goleiro(Jogador):
    # def __init__(self,nome,idade,camisa,posicao,gols,golsSofridos):
    def __init__(self,golsSofridos,*args,**kargs):
        # estudar isso, args retornar set, e kargs retorna dict
        super().__init__(*args,**kargs) 
        self.golsSofridos = golsSofridos

