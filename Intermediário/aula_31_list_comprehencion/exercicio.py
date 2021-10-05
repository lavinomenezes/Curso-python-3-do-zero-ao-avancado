""""
def conjunto(string,tam):
    tx = list()
    aux = ''
    for i in range(len(string)):
        aux += txt[i]
        if len(aux) == tam:
            tx.append(aux)
            aux = ''
    return tx
"""
def conjunto(string,replace,rep):
    aux = string.replace(replace+rep, f'{replace}*{rep}')
    aux = aux.split("*")
    aux = list(aux)
    return aux

txt = "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
l1 = [v for v in conjunto(txt,'9', '0')]
l3 = [txt[i:i+10] for i in range(0,int(len(txt)),10)]
l2 = '.'.join([v for v in l1])
print(l1)
print(l2)
print(l3)
