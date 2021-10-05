""""
# listas, tuplas, str -> sequancias ->iteraveis
l1 = [1,2,3,4,5,6] #iteravel
l1 = iter(l1) # transforma in iterador

print(next(l1))
print(next(l1))
print(next(l1))
lista = 'String' # iteravel
print(hasattr(l1,'__next__'))
for i in l1:
    print(i) #iterador"""
import sys
import time
lista = list(range(100))
print(lista)
print("Tamanho em bytes:", sys.getsizeof(lista))
def gera():
    r = []
    for n in range(100):
        yield n # gerador


g = gera()
print(g)
print(sys.getsizeof(g))
for v in g:
    print(v, end=' ')
