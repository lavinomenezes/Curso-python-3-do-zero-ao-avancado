"""""
uma classe é dona de objetos de outra classe
"""""

class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self,cidade,estado):
        self.enderecos.append(Endereco(cidade,estado))

    def lista_enderecos(self):
        for i in self.enderecos:
            print(i.cidade,i.estado)
    def __del__(self):
        print(f"{self.nome} foi apagado")

class Endereco:
    def __init__(self,cidade,estado):
        self.cidade = cidade
        self.estado = estado
    def __del__(self):
        print(f"{self.cidade} foi apagado")
