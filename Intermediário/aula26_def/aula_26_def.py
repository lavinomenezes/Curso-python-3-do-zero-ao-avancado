""""
funções - def em python
"""
def saudacao(msg='olá',nome='usuáro'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)
