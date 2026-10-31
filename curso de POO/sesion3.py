a = 10
b = 9
c = 1
print(not(a == b and a > c))

print("123".isdigit()) # evalúa que la cadena sean solo digítps (números)

print("12f3".isdigit())

print("skfsdlf".isalpha()) # evalúa que hayan solo letras

print("skfsdlf".isalnum()) # evalúa que hayan solo letras y números, no carácteres y espacios

# con entradas
texto = input("ingrese un dato")
print(type(texto))
numero = int(texto)
print(type(numero)) # muestra el tipo de dato de la variable número

print(texto.strip()) # Elimina los espacios en blanco al inicio y al final

print(texto.lower()) # convierte el texto en minusculas

print(texto.upper()) # convierte el texto en mayúscula

print(texto.replace("HOLA", "ADIOS")) # reemplaza una palabra con ADIOS

print(texto.startswith(" HOLA")) # verifica verifica si el texto comienza con " HOLA"

print(texto.endswith(" MUNDO")) # verifica si el texto termina en " MUNDO"

