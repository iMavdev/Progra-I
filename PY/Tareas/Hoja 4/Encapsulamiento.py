class CuentaBancaria:
    def __init__(self, numerodecuenta,titular,saldo):
        self.numerodecuenta = numerodecuenta
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, cantidad):
        if cantidad >= 0:
            self.__saldo = cantidad
        else:         
            print("ERROR: ¡El saldo no puede ser negativo!")

    def depositar(self, monto):
        if monto <= 0:
            print("ERROR: ¡La cantidad a depositar debe ser mayor que cero!")
        else:
            if monto > 0:
                self.saldo += monto
                print(f"Depósito realizado. Saldo actual: {self.saldo} Quetzales.")
        print(f"Gracias por utilizar nuestro sistema bancario. Vuelva pronto.")

    def retirar(self, monto):
        if monto <= 0:
            print("ERROR: ¡La cantidad a retirar debe ser mayor que cero¡")
        else:
            if monto > self.saldo:
                print("Saldo insuficiente para realizar el retiro.")
            else:
                self.saldo -= monto
                print(f"Retiro realizado. Saldo actual: {self.saldo} Quetzales.")
        print(f"Gracias por utilizar nuestro sistema bancario. Vuelva pronto.")
    

    def consultar_saldo(self):
        return self.__saldo

print(f"-----------------------------------------------")
print(f"BIENVENIDO A SISTEMA BÁSICO DE CUENTA BANCARIA")
print(f"-----------------------------------------------")

#Solicitud de datos al usuario para crear una cuenta bancaria.
print(f"Ingrese los datos para crear la cuenta bancaria")
numerodecuenta = input("Ingrese el número de cuenta: ")
titular = input("Ingrese el nombre del titular de la cuenta: ")
saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))#float convierte el valor ingresado a decimal
cuenta = CuentaBancaria(numerodecuenta, titular, saldo_inicial) #la variable cuenta es un objeto de la clase CuentaBancaria y se le pasan los datos ingresados por el usuario como argumentos al constructor de la clase.
print(f"Cuenta creada para {cuenta.titular}, con número de cuenta {cuenta.numerodecuenta} y con saldo inicial de {cuenta.saldo} Quetzales.")


monto_deposito = float(input("Ingrese la cantidad a depositar: "))
cuenta.depositar(monto_deposito)
print(f"Consulta de saldo: {cuenta.consultar_saldo()} Quetzales.")


monto_retiro = float(input("Ingrese la cantidad a retirar:"))
cuenta.retirar(monto_retiro)
print(f"Consulta de saldo: {cuenta.consultar_saldo()} Quetzales.")

cuenta.saldo=1
print (cuenta.saldo)