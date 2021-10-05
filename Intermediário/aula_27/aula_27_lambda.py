def func(X,Y):
    return X * Y


var = func(2, 2)
a = lambda X, Y:X*Y
print(var)
print(a(2,2))
lista = [   ['p1', 13],
            ['p2', 5],
            ['p3', 67],
            ['p4', 23],
            ['p5', 9],
         ]
#def func2(item):
#    return item[1]
#lista.sort(key=func2)
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)
print(sorted(lista, key=lambda  item: item[0]))
