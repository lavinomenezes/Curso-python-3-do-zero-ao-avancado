"""
polimorfismo é o principio que permite que classes derivadas de uma esma supercalsse tenham metodos iguais
(de mesma asinatura) mas comportamentos diferentes.
mesma assinatura = mesma quantidade e tipo de parâmetros
"""

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self,msg): pass

class B(A):
    def fala(self,msg):
        print(f'b está falando {msg}')

class C(A):
    def fala(self,msg):
        print(f'c está falando {msg}')

b = B()
c = C()
b.fala('um assunto')
c.fala('outro assunto')