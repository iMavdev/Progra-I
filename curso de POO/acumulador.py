#Acumuladro de Suma
total = 0 #Inicializar la variable

while True:
    valor = input ("Ingrese un número (o no escriba nada para terminar): ")
    if valor == "":
        break
    total+= int(valor)

print (f"La suma total es: {total}")

#Acumulador con multiplicación
total = 1

while True:
    valor = input ("Ingrese un número (o no escriba nada para terminar): ")
    if valor == "":
        break
    total = total * int(valor)

print (f"La multiplicación es: {total}")

#Complemento a 2 Investigar