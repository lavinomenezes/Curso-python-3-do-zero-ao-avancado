from eletronico import Eletronico
from log import LogMixin
class Smartphone(Eletronico,LogMixin):
    def __init__(self,nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f"{self._nome} nao está ligado"
            self.log_info(info)
            return

        if self._conectado:
            ERROR = f"{self._nome} Ja esta conectado"
            print(ERROR)
            self.log_error(ERROR)
            return
        info = f"{self._nome} Esta conectado"
        print(info)
        self.log_info(info)
        self._conectado = True


    def desconectar(self):
        if not self._conectado:
            ERROR = f"{self._nome} não esta conectado"
            print(ERROR)
            self.log_error(ERROR)
            return
        info = f"{self._nome} foi desligado com suscesso"
        print(info)
        self.log_info(info)
        self._conectado = False
