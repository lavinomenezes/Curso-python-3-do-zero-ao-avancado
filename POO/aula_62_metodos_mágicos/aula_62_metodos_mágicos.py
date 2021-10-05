class A:
    def __new__(cls, *args, **kwargs):
        cls.nome = 'lavino'
        return super().__new__(cls)
    def __init__(self):
        print('eu sou o INIT')
    pass

a = A()