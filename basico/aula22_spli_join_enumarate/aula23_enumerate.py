lista = [['lavino','elaine','wanessa'],['barbara','guilherme','roberta'],['bryan','catarina','marcelinho']]
enum = enumerate(lista)
#print(list(enum))
#print(lista[0][0])
#for i, v in enumerate(lista):
 #   print(v[0],v[1])
#for i in range(len(lista)):
#    for j in range(len(lista)):
#        print(lista)
for v in enumerate(lista):
    valor, dado = v
    print(valor, dado)
    n1,n2,n3 = dado
    print(n1)