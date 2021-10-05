"""
Split, Join, Enumerate Python

txt = "O brasil é o pais do futebol, o brasil é corno, brasil é foda"
lista1 = txt.split()
lista2 = txt.split(',')
print(lista1)
print(lista2)
palavra = ''
contagem = 0
for n in lista1:
    qtd = lista1.count(n)
    if qtd > contagem:
        contagem = qtd
        palavra = n
print(f"a palavra que mais apareceu é '{palavra}' {contagem} vezes")

print(' '.join(lista1))
"""
txt = "O brasil é o pais do futebol, o brasil é corno, brasil é foda"
for v, c in enumerate(txt):
    print(txt[v])
lista = ['lavino','elaine', 'wanessa']
A, B, C = lista
print(C)