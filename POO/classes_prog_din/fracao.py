#atributos
# 1. numerador. 2 denominador
# métodos
# somar; subtrair; multiplicação; dividor; inverter*; simplificar
class Fracao:

    def __init__(self,num,den):#(__init__)cosntrutor da clase / self primeiro argumento o OBJETO que está sendo construido
        self.num = num
        if den == 0:
            self.den = 1
        else:
            self.den = den
        pass
    def soma(self,outra):
        pass

    def multiplicar(self,outra):
        num = self.num * outra.num
        den = self.den * outra.den
        return Fracao(num,den)

    def dividr(self,outra):
        return self.multiplicar(outra.inverter())

    def inverter(self):
        return Fracao(self.den,self.num)

    def negar(self):
        return Fracao(-self.num,self.den)
