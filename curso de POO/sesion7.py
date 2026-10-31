def sumar(): #Diferencias IF, While, For
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))

    sumar=n1+n2

    print (f"El resultado de la suma es {sumar}")

def restar():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))

    restar=n1-n2

    print (f"El resultado de la suma es {restar}")

def multiplicar():
    n1 = int (input("Ingrese el primer número: "))
    n2 = int (input("Ingrese el segundo número: "))

    multi=n1*n2

    print(f"El resultado de la multiplicación es {multi}")

def dividir():
    n1 = int (input("Ingrese el primer número: "))
    n2 = int (input("Ingrese el segundo número: "))

    if n2 == 0:
        print("ERROR: No se puede dividir entre cero.")
    else:
        div=n1/n2
        print(f"El resultado de la división es {div}")
    

while True:
    print ("\n=============Calculadora================")
    print ("1 - SUMAR")
    print ("2 - RESTAR")
    print ("3 - MULTIPLICAR")
    print ("4 - DIVIDIR")
    print ("5 - SALIR")

    opcion=input("Seleccione una opción: ")
    if opcion == "1":
        sumar()
    elif opcion == "2":
        restar()
    elif opcion == "3":
        multiplicar()
    elif opcion == "4":
        dividir()
    elif opcion == "5":
        print("Órale")
        break
    else:
        print ("Opción Inválida")
