from conta import Conta

class ContaPoupança(Conta):
    def sacar(self,valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor


a = ContaPoupança(558,1113-2,700)
a.depositar(700)
a.sacar(500)
a.detalhes()