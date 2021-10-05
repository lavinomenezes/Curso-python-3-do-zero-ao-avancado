"""
operadores lógicos
and, or, not
in e not in
"""
# verdadeiro e verdadeiro
comp1 = 1
comp2 = 1
comp3 = 2
comp4 = 3

print(comp1 == comp2  and comp3 == comp4)
print(comp1 == comp2  or comp3 == comp4)
print(not(comp1 == comp2  or comp3 == comp4))

nome="lavino menezes"

if 'a' in nome and 'w' not in nome:
    print("existe a letra 'a' e não existe 'w' no seu nome")
else:
    print("as letras não existe no seu nome")

