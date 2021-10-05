class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("Falando")


class Cliente(Pessoa):
    pass


class Aluno(Pessoa):
    pass


class ClienteVIP(Cliente):
    pass