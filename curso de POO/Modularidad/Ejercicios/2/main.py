from persona import Persona 
from cuenta import Cuenta
from tc import TC

persona1 = Persona("Leonardo")
cuenta1 = Cuenta("579852")

persona1.relacioncuenta = cuenta1

print(f"Cuenta creada a nombre de {persona1.nombre} con saldo: {persona1.relacioncuenta.saldo}")

#Deposito de dinero en la cuenta
persona1.relacioncuenta.saldo = 1000
print(f"Deposito efectuado: El saldo de la cuenta de {persona1.nombre} es: {persona1.relacioncuenta.saldo}")

#Retiro de dinero en la cuenta
persona1.relacioncuenta.saldo = persona1.relacioncuenta.saldo - 500
print(f"Retiro efectuado: El nuevo saldo de la cuenta de {persona1.nombre} es: {persona1.relacioncuenta.saldo}")

#Tarjeta de crédito
tc1 = TC("10202507")

#Pago a TC
persona1.relaciontc = tc1
persona1.relaciontc.saldo = 500

print(f"Pago efectuado de: {persona1.relaciontc.saldo} a la tarjeta de crédito de {persona1.nombre} numero de tarjeta {persona1.relaciontc.numero}")
