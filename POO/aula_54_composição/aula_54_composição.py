from classes import Cliente, Endereco

c1 = Cliente('elaine', 25)
c1.inserir_endereco("João pessoa", "MG")
c1.lista_enderecos()
print()
c2 = Cliente('Maria', 55)
c2.inserir_endereco("Belo horizonte", "PB")
c2.inserir_endereco("São paulo", "RJ")
print(c2.nome)
c2.lista_enderecos()
print()
c3 = Cliente('wanessa', 33)
c3.inserir_endereco('Para', 'PR')
print(c3.nome)
c3.lista_enderecos()
print()

