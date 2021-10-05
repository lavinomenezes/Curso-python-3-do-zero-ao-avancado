from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('camisa',50)
p2 = Produto('Galaxy s21',4000)
p3 = Produto('caneca',15)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p1)
carrinho.lista_produtos()
print(carrinho.soma_total())