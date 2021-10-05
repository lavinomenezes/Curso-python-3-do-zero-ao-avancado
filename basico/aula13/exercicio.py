"""
num = input("digite um numero inteiro: ")

if num.isnumeric():
    num = int(num)
    if num%2 != 0:
        print(f" o nuemero {num} é impar")
    elif num%2 == 0:
        print(f" o nuemero {num} é par")
else:
    print("entrada invalida, informe um numero inteiro")

hora = input("digite apenas a horas: ")

if hora.isnumeric():
    hora = int(hora)
    if hora >=0 and hora <=11:
        print("bom dia, o sol amanheceu na fazendinha")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde acorda vagabundo")
    elif hora >=18 and hora <=23:
        print("acorda quase hora do BBB")
else:
    print("entrada invalida, infome apenas a hora entre 0 e 23")

"""
nome = input("qual o seu nome?: ")

if len(nome) <=4:
        print("teus pais tem preguiça")
elif len(nome) > 4 and len(nome) < 7:
        print("nome biblico")
elif len(nome) > 6 :
        print("eu vou comer seu cu no uno")


