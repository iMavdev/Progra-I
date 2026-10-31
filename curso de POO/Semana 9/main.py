from usuario import Usuario
from cuenta import Cuenta

usuario1=Usuario("Juan Perez", "juan.perez@example.com")
cuenta1=Cuenta(1000)
usuario1.cuenta = cuenta1

print("Usuario:", usuario1.nombre)
print("Correo:", usuario1.correo)
print("Saldo inicial de la cuenta:", usuario1.cuenta.saldo)      

usuario1.depositar_user(500)
print ("Saldo después del depósito: ", usuario1.cuenta.saldo)

usuario1.retirar_user(200)
print ("Saldo después de retirar: ", usuario1.cuenta.saldo)