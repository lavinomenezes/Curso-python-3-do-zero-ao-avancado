class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def desconto(self,percentual):
        self.preco = self.preco - (self.preco*(percentual/100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,valor):
        self._nome = valor.lower()

    #Getter
    @property
    def preco(self):
        return self._preco
    #Setter
    @preco.setter
    def preco(self,valor):
        if isinstance(valor,str):
            valor = float(valor.replace('R$',''))

        self._preco = valor



p1 = Produto('CAMISA',50)
p1.desconto(10)
p2 = Produto('Jogo','R$30')
p2.desconto(20)
print(p1.preco)
print(p2.preco)
print(p1.nome)