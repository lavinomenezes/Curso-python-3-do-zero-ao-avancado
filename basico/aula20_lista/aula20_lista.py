""""
Lista em python
fatiamento
append - adiciona no final
insert - inseri onde for determinado
pop - retira o ultimo elemento
del - remove uma quantidade variada de elementos
clear
extend - soma listas
min - valor minimo da lista
max - valor máximo da lista
range

booleanos = True
inteiros = 10
flutuantes = -10.10
texto = 'valor'
lista = [1,2,3,4,'lavino', True, 10.5]
lista2 = ['a','b','c','d','e']

while n < 5:
    X = input()
    lista.append(X)
    n +=1
print(lista)

l3 = ['solk', 2, True, 20.0]
l1 = [1,2,3,4,5,6,7,8,9]
l2 = list(range(1,10))
del(l1[3])
n = 0
print(l2)
print(l1)
print(max(l1))
print(min(l1))
"""
secreto = 'perfume'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print("you lose")
        break
    letra = input("DIGITE UMA LETRA:")

    if len(letra) > 1:
        print("não vale, digite uma letra")
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f' a letra {letra}, existe na palavra')
    else:
        print(f' a letra {letra}, não existe na palavra')
        digitadas.pop()
    secreto_temporario = ''
    for letra_s in secreto:
        if letra_s in digitadas:
            secreto_temporario += letra_s
        else:
            secreto_temporario += '*'


    if secreto_temporario == secreto:
        print("vc acertou")
        break
    else:
        print(secreto_temporario)
    if letra not in secreto:
        chances -= 1

    print(f"voce tem {chances} restantes")
