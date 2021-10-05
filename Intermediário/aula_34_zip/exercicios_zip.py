"""""
considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

se uma lista for maior que a outra, a soma só vao considerar o tamanho da menor

lista_a = [1,2,3,4,5,6,7]
lista b = [1,2,3,4]

lista soma = [2,4,6,8]
"""""

lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

#l1 = list(zip(lista_b,lista_b))
#ls = [sum(l1[i]) for i in range(len(l1))]
ls = [X+Y for X, Y in zip(lista_a,lista_b)]
print(ls)
