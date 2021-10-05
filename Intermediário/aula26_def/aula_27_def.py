"""
funcoes def em python *args **kwargs

def func(a,b,c,d,e, nome = None, a6 = None):
    print(a,b,c,d,e, nome, a6)
    return a, b

var = func(1,2,3,4,5,'luiz', 5)
"""

lista = [1,2,3,4,5]
n1, n2, *n = lista
print(n1,n2,n)
print(*lista,end='')
print(*lista, sep='-')

def fuck(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
fuck(1,2,3,4,5)
def you(*args,**kwargs):
    args = list(args)
    print(args)
    print(kwargs)
    idade = kwargs.get('idade')
    if idade:
        print(idade)
    else:
        print("idade não existe")
  #  print(type(args[0]))
teste = 'dia 5'
teste.split()
you(*lista, nome = 'lavino', sobrenome = "menezes", idade=18)