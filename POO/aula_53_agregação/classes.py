""""
a classe precisa de outra classe
"""""
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self,produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for i in self.produtos:
            print(i.nome,i.valor)

    def soma_total(self):
        s = 0
        for i in self.produtos:
            s += i.valor
        return s


class Produto:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor