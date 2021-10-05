"""
public,
protected, private (public_)
__ privado(_NomeClasse_nomeatributo
"""
class BaseDeDados:
    def __init__(self):
        self.__dados = {} #publico, com _ antes fica privado __ com 2 underlines fica protegido
    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id,nome)

        pass
    def apaga_cliente(self,id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1,'elaine')
bd.inserir_cliente(2,'barbara')
bd.inserir_cliente(3,'lorenna')
bd.lista_clientes()
print(bd.dados)
print(bd._BaseDeDados__dados)
print("*"*30)
bd.apaga_cliente(2)
bd.lista_clientes()
