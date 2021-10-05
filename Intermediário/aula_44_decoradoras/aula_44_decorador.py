def patrao(funcao):
    def empregado():
        print('Agora estou decorado.')
        funcao()
    return empregado
@patrao
def oi():
    print('oi')


oi()