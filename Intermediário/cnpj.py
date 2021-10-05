txt = '04.252.011/0001-10'
l1 = list()
aux = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
for i in range(0, len(txt) - 2):
    if txt[i].isnumeric():
        l1.append(int(txt[i]))
print(l1)
s = sum(list(map(lambda x, y: x * y, l1, aux[1:])))
x = 11 - (s % 11)
x = 1 if x < 9 else 0
l1.append(x)
ss = sum(list(map(lambda x, y: x * y, l1, aux)))
y = 11 - (ss % 11)
y = 1 if y < 9 else 0
l1.append(y)
print(txt)
print(l1)
if int(txt[-1]) != l1[-1] or int(txt[-2]) != l1[-2]:
    print("CNPJ invalido")
else:
    print("Cnpj válido")
