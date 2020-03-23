from .pessoa import Pessoa

class Tecnico(Pessoa):
    def __init__(self,nome,idade,experiencia):
        super().__init__(nome,idade)
        self.experiencia = experiencia