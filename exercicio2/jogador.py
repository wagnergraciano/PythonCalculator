from .pessoa import Pessoa
from random import randint

class Jogador(Pessoa):

    def __init__(self,nome,idade,camisa,posicao,gols):
        super().__init__(nome,idade)
        self.camisa = camisa
        self.posicao = posicao
        self.gols = gols

    def chutar(self,goleiro):
        if (randint(0,99) <= 65):
            self.gols += 1
            goleiro.golsSofridos += 1
