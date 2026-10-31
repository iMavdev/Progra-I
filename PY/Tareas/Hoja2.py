class CuentaBancaria:

    def __init__(self, titular, saldo):
        #Atributos de la clase
        self.titular = titular
        self.saldo = saldo

        #Métodos de la clase
        #Método para realizar un depósito
    def depositar(self, cantidad):
        self.saldo += cantidad #+= significa que se suma a la variable saldo el valor de cantidad
        print(f"Se han depositado {cantidad} Quetzales. Saldo actual: {self.saldo}")

    #Método para realizar un retiro
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
        else:
            self.saldo -= cantidad #-= significa que se resta a la variable saldo el valor de cantidad
            print(f"Se han retirado {cantidad} Quetzales. Saldo actual: {self.saldo}")

print(f"-----------------------------------------------")
print(f"BIENVENIDO A SISTEMA BÁSICO DE CUENTA BANCARIA")
print(f"-----------------------------------------------")

#Solicitud de datos al usuario
titular = input("Ingrese el nombre del titular de la cuenta: ")
saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))#float convierte el valor ingresado a decimal
cuenta = CuentaBancaria(titular, saldo_inicial) #la variable cuenta es un objeto de la clase CuentaBancaria
print(f"Cuenta creada para {cuenta.titular} con saldo inicial de {cuenta.saldo} Quetzales.")

depositar_cantidad = float(input("Ingrese la cantidad a depositar: "))
cuenta.depositar(depositar_cantidad)
print(f"Depósito realizado. Saldo actual: {cuenta.saldo} Quetzales.")

retirar_cantidad = float(input("Ingrese la cantidad a retirar: "))
if retirar_cantidad > cuenta.saldo:
    print("Saldo insuficiente para realizar el retiro.")
else:
    cuenta.retirar(retirar_cantidad)
    saldo_final = cuenta.saldo
    print(f"Saldo final: {saldo_final} Quetzales.")
    print(f"Retiro realizado. Saldo actual: {cuenta.saldo} Quetzales.")

print(f"Gracias por utilizar nuestro sistema bancario. Vuelva pronto.")

print(f"--------------------------------------------------------")
print(f"BIENVENIDO A SISTEMA BÁSICO DE REGISTRO DE COMPUTADORAS")
print(f"--------------------------------------------------------")

class Computadora:
    def __init__(self, marca, ram):
        self.marca = marca
        self.ram = ram
    #Atributos de la clase
    def informacion (self):
        print (f"La marca de la computadora es: {self.marca}, La cantidad de memoria RAM es: {self.ram} GB")

Computadoras = [] #Variable tipo vector (array)
#Solicitar datos
cantidad = int (input("Cuantas computadoras desea ingresar: "))
for i in range (cantidad):
    print (f"\nComputadora No {i+1}") #{i+1} contador en el que dice que empiece en 1 y no en 0
    marca = str(input ("Ingrese la marca de la computadora: "))
    ram = float(input ("Ingrese la cantidad de memoria RAM (en GB): "))
    #Construir el objeto e introducirlo dentro de variable y luego se introduce dentro de array
    c=Computadora(marca,ram)
    #El objeto c lo ingresamos al array Computadoras = [c] Qué es Array? Es una estructura de datos que permite almacenar múltiples valores en una sola variable. En este caso, estamos almacenando objetos de la clase Computadora en el array Computadoras.
    Computadoras.append(c) #Append adicionar algo a Computadoras

#Crear el listado de computadoras registradas
print(f"\nLista de computadoras registradas: {len(Computadoras)}") #{len(Computadoras)} devuelve la cantidad de objetos en el array Computadoras
for c in Computadoras:  #qué es for c in Computadoras? Es un bucle que recorre cada objeto c en el array Computadoras y ejecuta el método informacion() para cada uno de ellos.
    c.informacion()
print (f"\nGracias por utilizar nuestro sistema de registro de computadoras.")