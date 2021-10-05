from dados import produtos, pessoas, lista
def aumento(p):
    p['preco'] = round(p['preco']*1.05,2)
    return p


n1 = map(lambda x: x*2, lista)

d1 = map(aumento, produtos)
for i in d1:
    print(i)
print(list(n1))
print(produtos)