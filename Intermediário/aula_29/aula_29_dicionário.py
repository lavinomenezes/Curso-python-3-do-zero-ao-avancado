""""
d1 = {
    'chave1': 'valor',
    'chave2': 'outro',
}


d1['chave3'] = 'agora existe'
d1['chave4'] = 'nova'
d1.update({'chave5':'novonovo valor'})
print(d1)
print('valor' in d1.values())
print('chave2' in d1.keys())
print('chave1' in d1)
print(len(d1))
for i in d1.keys():
    print(i, end= '')
for i in d1.values():
    print(i)
for i, c in d1.items():
    print(i, c)
"""""
clientes = {
    'cliente1':{
        'nome': 'Luiz',
        'Sobrenome': 'otavio'
    },
    'cliente2':{
        'nome': 'Lavino',
        'Sobrenome': 'Menezes'
    },
}
for i, k in clientes.items():
    print(i.upper())
    for j, c in k.items():
        print(f'{j} = {c}')
V = clientes.copy()
print(V)