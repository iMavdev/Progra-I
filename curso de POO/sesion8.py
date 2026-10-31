class CuentaBancaria:
    def __init__(self, propietario, saldo):
        self.__propietario = propietario
        self.__saldo = saldo

    @property #Encapsulamiento
    def saldo (self):
        return self.__saldo

    @saldo.setter #Para modificar algo, en este caso el saldo.
    def saldo(self,nuevo_saldo):
        if nuevo_saldo < 1:
            print("No se puede establecer un saldo negativo o cero.")
        else:
            self.__saldo = nuevo_saldo

cuenta = CuentaBancaria("Juan", 1000)
print(cuenta.saldo)
cuenta.saldo=-2000
print(cuenta.saldo)

