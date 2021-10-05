"""
Operadores
== > >= < <= !=
"""
idade = """40"""
print(idade)
# print(2!=2)
numero = int(input("digite um numero: "))

if numero<0:
    print("valor negativo")
elif numero>10:
    print("numero muito alto")
else:
    print(f"o numero {numero} é valido")
