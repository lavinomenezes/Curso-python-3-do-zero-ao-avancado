CPF = input("Digite seu CPF: ")
test = list()
som = 0
X = Y = 0
dig1 = dig2 = 0
for i in CPF:
    if i == '.' or i =='-' or i ==' ':
        continue
    else:
        test.append(int(i))
for i in range(11,2,-1):
    som += (i-1) * test[-i]
X =  11 - (som%11)
dig1 = 0 if X > 9 else X
som = 0
for i in range(11,1,-1):
    som += (i) * test[-i]
X = 11 -(som%11)
dig2 = X
if dig1 == test[9] and dig2 == test[10]:
    print("CPF válido")
else:
    print("CPF INVÁLIDO")
