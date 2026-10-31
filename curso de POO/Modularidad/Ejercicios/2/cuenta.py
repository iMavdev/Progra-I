class Cuenta:
    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo
    