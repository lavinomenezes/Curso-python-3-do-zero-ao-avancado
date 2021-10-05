"""
teste = list()
teste.append("lavino")
teste.append(25)
galera = list()
galera.append(teste[:])
teste[0] = 'elaine'
teste[1] = 25
galera.append(teste[:])
print(galera)
************************************************************************************************************
galera = [['lavino', 25],['elaine', 25],['wanessa',32],['barbara',23]]
print(galera[0])
for p in galera:
    print(p[0])
************************************************************************************************************
"""
galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input("Digite o nome: ")))
    dado.append(int(input("Digite a idade: ")))
    galera.append(dado[:])
    dado.clear()
for M in galera:
    if M[1] >= 18:
        print(f'{M[0]} já pode ser preso(a)')
    else:
        print(f'{M[0]} ainda não pode ser preso(a) :(')
print(galera)