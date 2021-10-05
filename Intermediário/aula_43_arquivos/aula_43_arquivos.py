""""file = open('abc.txt', 'w+')
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')
file.seek(0,0)
print('lendo linhas: ')
print(file.read())
print('###############')
file.seek(0,0)
for linha in file.readlines():
    print(linha)

file.close()"""""
""""try:
    file = open('abc.txt', 'w+')
    file.write("Mamma mia")
    file.seek(0,0)
    print(file.read())
finally:
    file.close()

with open('abc.txt', "w+") as file:
    for i in range(10):
        file.write(str(i))

    file.seek(0)
    print(file.read())"""""
import os
os.remove('abc.txt')