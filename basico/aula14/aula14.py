"""
Formatando valores
:s - texto
:d - inteiros
:f numeros de ponto flutuante
:.(numero)f - quantidade de casas decimais (float) :.2f
:(Caractere)(> ou < ou ^)(Quantidade)(tipo -s,d ou f)
> - esquerda
< - direita
^ - centro

A = 10
B = 3
DIVISAO = A/B
print('{:.2f}'.format(DIVISAO))
print(f'{DIVISAO:.2f}')
"""
nome = "lavino menezes"

nome_f = '{:@>50}'.format(nome)
print(f"{nome:#^50}")
print(nome_f.upper())
print(nome_f.title())
#print(f'{A:0^10.2f}')

