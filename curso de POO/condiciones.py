edad = 5
if edad <= 5:
    print("es un  niño")
elif edad >= 13 and edad <= 19:
    print("es un adolecente")
else:
    print("es un adulto")

# ejercicio
print("ingrese un número")

num = float(input())

residuo = num%2


if residuo == 0:
    print("el número es par")
else:
    print("el número es impar")