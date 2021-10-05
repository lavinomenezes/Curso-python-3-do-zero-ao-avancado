"""""
count - Itertools

from types import  GeneratorType
var = ((x,y) for x,y in zip('Alo', 'Alo'))
print(isinstance(var,GeneratorType))
"""""
from itertools import count
from time import sleep

cotador = count(start=0,step=5)
for i in cotador:
    print(i)
    sleep(0.5)


