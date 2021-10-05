from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        pass

class B(A):
    def falar(self):
        print("B falando")
    pass

a = A()
a.falar()