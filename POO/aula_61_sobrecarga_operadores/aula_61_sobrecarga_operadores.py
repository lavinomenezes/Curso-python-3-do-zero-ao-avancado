"""
No python, o comportamento dos operadores é definido por métodos especiais.
vamos alterar o comportamento de operadores com classes definidas pelo usuário
"""

class Retalngulo:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class 'Retangulo({self.x},{self.y})'>"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retalngulo(novo_x,novo_y)

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

r1 = Retalngulo(10,20)
r2 = Retalngulo(10,20)
r3 = r1+r2
print(r3)