l1 = [1,2,3,4,5,6,7,8,9]
l2 = [var for var in l1]

l3 = [var*2 for var in l1]

l4 = [(v,v2) for v in l1 for v2 in range(3)]
l6 = ['maria', 'jose', 'mauro']
l5 = [v.replace('a', '@').upper() for v in l6]
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
l7 = [(x,y) for y,x in tupla]
l8 = list(range(100))
l9 = [v for v in l8 if v%3 == 0 if v%8 == 0]
l10 = [v if v%3 == 0 and v%8 == 0 else "não é" for v in l8 ]
print(l2)
print(l3)
print(l4)
print(l5)
print(l7)
print(l9)
print(l10)