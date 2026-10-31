#Esconder los datos que estan dentro de un sistema para que no esten expuestos
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
 
    @property
    def saldo(self):
        return self.__saldo
 
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("El saldo no puede ser negativo.")
 
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
 
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")
 
    def consultar_saldo(self):
        return self.__saldo
 
    def obtener_titular(self):
        return self.__titular
 
cuenta = CuentaBancaria("Juan Pérez", 1000)
print(f"Titular de la cuenta: {cuenta.obtener_titular()}")  
 
cuenta.depositar(500)
cuenta.retirar(300)
print(f"Saldo actual: {cuenta.consultar_saldo()}")