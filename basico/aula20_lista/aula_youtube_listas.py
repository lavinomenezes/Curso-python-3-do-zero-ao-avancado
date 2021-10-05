num = [2,5,9,1, 17,87,-14]
num[2] = 3
num.append(90)
print(num)
num.sort()
print(num)
num.insert(3,4)
print(num)
num.pop()
print(num)
if 5 in num:
    num.remove(5)
else:
    print("não tem 5")
print(num)
for c, v in enumerate(num):
    print(num[c+2])
print(len(num))