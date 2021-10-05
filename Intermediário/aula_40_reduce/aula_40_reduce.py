from dados import pessoas, produtos, lista
from functools import reduce

count = 0
for i  in lista:
    count+= i
print(count)
l1 = reduce(lambda ac, i:i['preco']+ac,produtos,0)
print(l1)