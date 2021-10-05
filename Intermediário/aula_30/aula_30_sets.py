"""
Conjuntos(sets): são similares as listas e decionários, ou seja é um conjunto de elementos que é adicionado a uma estrutura de dados
a diferenaça é que suporta apenas um tipo de elemento
#####################NÃO ACEITÃO ELEMENTOS DUPLICADOS###########################
add(adiciona);
update(atualiza);
celar(limpa);
discard();
union | (une)
intersection & (todos os elemntos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos
"""

s1 = {1,2,3,4,5,6}
s2 = set()
s2.add(1)
s2.add(2)
print(s2)
s1.discard(3)
print(s1)
s3 = set()
s3.update('Python') #não itera na ordem que foi passada
print(s3)
s4 = set()
s4.update([1,2,3,4,5], {4,5,6})
print(s4)
l1 = [1,1,1,2,2,2,3,4,5,6,78,78,'lavino', 'lavino']# utilizado para retirar elementos duplicados
l1 = set(l1)
print(l1)
s5 = {1,2,3,4,5,7}
s6 = {1,2,3,4,5,6}
s7 = s5 | s6
print(s7)
print(s5 & s6) # interssection
print(s5 - s6) # diferrence, a ordem importa
print(s5 ^ s6) # symmetric_difference
