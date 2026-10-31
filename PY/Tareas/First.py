# EJERCICIO 1
print ("Bienvenido al programa de operaciones")
print ("Ingrese dos números con decimales")

# ENTRADAS
# Se solicita al usuario ingresar datos
n1 = float (input("Ingrese el primer número"))
n2 = float (input("Ingrese el segundo número"))

# PROCESOS Y SALIDAS
# Operación de suma
suma=n1+n2
print ("la suma es: ", suma)

# Operación de resta
resta=n1-n2
print ("la resta es: ", resta)

# Operación de multiplicación
multi=n1*n2
print ("la multiplicación es: ", multi)

# Operación de división
div=n1/n2
print ("la división es: ", div)

# Calculando residuo
res=n1%n2 # Utilizo el operador de módulo % para calcular residuos
print ("el residuo es: ", res)

print ("-----------------------FIN PROGRAMA 1------------------------------")

# EJERCICIO 2
#ENTRADA
while True: # Ciclo para repetir el dato que ingrese el usuario, hasta que escriba el correcto
        dato = input ("Ingrese un dato: ")
        # PROCESO
        if dato.isdigit(): # Función para evaluar si los datos ingresados por el usuario, son números enteros
            num= int(dato)
            break
        else:
            # SALIDA
            print ("El dato ingresado no es un número. Intente de nuevo")
print (f"El dato ingresado, corresponde a un número entero: {num}, gracias")
print ("-----------------------FIN PROGRAMA 2-----------------------------")

# EJERCICIO 3
# ENTRADAS
print ("Ingrese 5 nombres")
name1=str(input("Ingrese el primero"))
name2=str(input("Ingrese el segundo"))
name3=str(input("Ingrese el tercero"))
name4=str(input("Ingrese el cuarto"))
name5=str(input("Ingrese le quinto"))

# PROCESOS
allname= [name1,name2,name3,name4,name5] # Vectores o listas

# SALIDAS
print (f"los nombres guardados son: {allname}")
print ("-----------------------FIN PROGRAMA 3-----------------------------")

# EJERCICIO 4
# PROCESOS
class Verificarprimo: # Clase para manejar la lógica de números primos
        # Función es_primo = método
    def es_primo(self, n): # Función que recibe un número 'n' y determina si es primo. Retorna True(verdadero) si es primo, o False(falso) si no lo es
     
        if n<=1: # Los números menores o iguales a 1 no son primos
          return False

        # Ciclo 'for' para comprobar si 'n' es divisible por x número
        # Desde 2 hasta n - 1.

        for i in range(2, n):
            # Si el residuo de la división es 0, significa que tiene otro divisor
            if n%i==0: # Toma el residuo de la división (==) Es comparador
                return False # Encontró un divisor, por lo tanto NO es primo

        # Si el ciclo termina sin encontrar divisores, sí es primo
        return True

if __name__ == "__main__":
    # Creo un objeto a partir de la clase
    verificador = Verificarprimo()

    # Solicita el número al usuario
    # Convierte la entrada a entero
    num_user = int (input("Ingrese un número: "))

    # Llama a la función usando el objeto y evalua el resultado
    resultado = verificador.es_primo(num_user)

    # Muestra el resultado usando una condición
    if resultado: 
        print(f"El número {num_user} ES primo.")
    else:
        print(f"El número {num_user} NO es primo")

print ("-----------------------FIN PROGRAMA 4-----------------------------")

# EJERCICIO 5
# PROCESOS
class Perro: # Se crea la Clase

    def __init__(self, nombre, edad): # Se define y construye el objeto

        # Guarda los datos
        self.nombre=nombre
        self.edad=edad

    #Define método dentro de la clase
    def hablar(self): # SALIDAS
        print (f"Hola humanos, mi nombre es {self.nombre} y tengo {self.edad} años")

Dog = Perro("Toby", 10)
Dog.hablar()

print ("-----------------------FIN PROGRAMA 5-----------------------------")