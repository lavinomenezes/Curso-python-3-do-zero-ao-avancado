class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeclass = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclass} Falando....')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclass} comprando....')


class Aluno(Pessoa):
    pass


class ClienteVIP(Cliente):
    def falar(self):
        super().falar()
        print("outra coisa")