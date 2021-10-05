def func(nome):
   return f'ola {nome}'
def func2(funcao,*args,**kwargs):
    return func(*args,**kwargs)
def func3(nome,saudacao):
    return f'{nome} {saudacao}'
exe = func2(func('luiz'), 'luiz')
print(exe)