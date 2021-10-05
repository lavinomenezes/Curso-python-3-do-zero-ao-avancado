l1=[
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {X:Y for X,Y in l1}
print(d1)
d1 = {X.upper():Y*2 for X,Y in l1}
print(d1)

d1 = {X:Y*2 for X,Y in enumerate(range(5))}
print(d1)
d1 = {X for X in range(5)}
print(d1)
d1 = {f'chave{x}':x**2 for x in range(5)}
print(d1)