"""
while usado para repetição enquanto condição for verdadeira
continue, reinicia o loop
break

nome = ''
while len(nome) <=0 :
    nome = input("qual seu nome? \n")
y = int(input("Que numero deseja pular de 0 a 9?"))
x=0
while x < 10:
    if x == y:
        x += 1
            break
    print(x)
    x += 1
print('acabou')


x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'({x}, {y})')
        y += 1

    x += 1


print('Acabou!')
"""
print("##bem vindo a calculadora##")
while True:
    A = (input("Digite o primeiro numero"))
    B = (input("Digite o segundo numero"))
    op = input("digite a opeção que deseja realizar \n Soma + \n Subtração - \n Divisão / \n multiplicação")


    if not A.isnumeric() and not B.isnumeric():
        print("digite uma entrada válida")
        continue
    A = float(A)
    B = float(B)
    if op == '+':
        print("A soma é igual a: ", A + B)
    elif op == '-':
        print("A subtracao é igual a: ", A - B)
    elif op == "/":
        print("A Divisão é igual a: ", A/B)
    elif op == "*":
        print("A Divisão é igual a: ", A*B)

