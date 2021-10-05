class Pessoa:
    ano_atual = 2019
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls,nome,ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome,idade)

p1 = Pessoa('Lavino',25)
print(p1.idade)
p1.get_ano_nascimento()
p2 = Pessoa.por_ano_nascimento('Elaine',1995)
print(p2.idade)