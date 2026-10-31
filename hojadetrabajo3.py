#Ejercicio 1...
print("Operaciones matemáticas y residuo")
n1= int(input("Ingrese el primer número: "))
n2= int(input("Ingrese el segundo número: "))

print(f"La suma es: {n1+n2}")
print(f"La resta es: {n1-n2}")
print(f"La multiplicación es: {n1*n2}")
print(f"La división es: {n1/n2}")
print(f"El residuo es: {n1%n2}")

#Ejercicio 2...
print("Determinación de la etapa de vida")
edad= int(input("Ingrese su edad: "))

if 0 <= edad <= 12:
    print("Se encuentra en la etapa de niñez")
elif 13 <= edad <= 17:
    print("Se encuentra en la etapa de adolescencia")
elif 18 <= edad <= 59:
    print("Se encuentra en la etapa de adultez")
else:
    print("Se encuentra en la etapa de vejez")

#Ejercicio 3...
print("Validación de dato")
dato = input("Ingrese un dato: ")
while not str(dato).isdigit(): #not str(dato).isdigit() evalua si el dato ingresado por el usuario es un número o no, si no lo es, se repite el ciclo
    print("Dato inválido. Por favor, ingrese un número.")
    dato = input("Ingrese un dato: ")

#Ejercicio 4...
print("Tabla de multiplicar")
n1=int(input("Ingrese un número: "))

for i in range(1, 13): #range(1, 13) genera una secuencia de números del 1 al 12, que se utilizará para multiplicar el número ingresado por el usuario (n1) y mostrar la tabla de multiplicar correspondiente.
    resultado = n1 * i
    print(f"{n1} x {i} = {resultado}")

#Ejercicio 5...
print("Ingrese 5 nombres")
name1=str(input("Ingrese el primero: "))
name2=str(input("Ingrese el segundo: "))
name3=str(input("Ingrese el tercero: "))
name4=str(input("Ingrese el cuarto: "))
name5=str(input("Ingrese el quinto: "))

allname= [name1,name2,name3,name4,name5] # Verifica que los nombres ingresados por el usuario se almacenan en una lista llamada allname, que luego se puede utilizar para realizar búsquedas o mostrar los nombres ingresados.
print(f"Los nombres guardados son: {allname}")

#Buscar un nombre en la lista
nombre_buscar = input("Ingrese el nombre a buscar: ")
if nombre_buscar in allname:
    print(f"El nombre {nombre_buscar} se encuentra en la lista.")
else:
    print(f"El nombre {nombre_buscar} no se encuentra en la lista.")

#Ejercicio 6...
print("Validación de nombre")
while True: #While true crea un bucle infinito que se repetirá hasta que se cumpla la condición de salida (break) dentro del bucle. Esto permite al usuario ingresar un nombre válido sin tener que reiniciar el programa.
    nombre = input("Ingrese un nombre: ")
    if len(nombre) >= 3: #len() evalua la cantidad de caracteres que tiene el nombre ingresado por el usuario
        print("Nombre válido.")
        print(f"El nombre ingresado tiene {len(nombre)} caracteres.")
        break
    else:
        print("El nombre debe tener al menos 3 caracteres. Por favor, ingrese un nombre válido.")
        
        
#Ejercicio 7...
print("Determinación de número primo")
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1): #int(numero**0.5) + 1 calcula la raíz cuadrada del número ingresado por el usuario y se utiliza para optimizar la verificación de si el número es primo o no. Esto se debe a que un número no puede tener factores mayores que su raíz cuadrada.
        if numero % i == 0: #numero % i == 0 evalúa si el número ingresado por el usuario es divisible por i, lo que indica que no es un número primo. Si se encuentra un divisor, la función devuelve False y termina la verificación.
            return False
    return True

numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

#Ejercicio 8...
print("Conversión de temperatura")
def convertir_temperatura(valor, tipo):
    if tipo == "Celsius":
        return (valor * 9/5) + 32  # Convertir de Celsius a Fahrenheit y la operación (valor * 9/5) + 32 es la fórmula para convertir una temperatura de grados Celsius a grados Fahrenheit.
    elif tipo == "Fahrenheit":
        return (valor - 32) * 5/9  # Convertir de Fahrenheit a Celsius y la operación (valor - 32) * 5/9 es la fórmula para convertir una temperatura de grados Fahrenheit a grados Celsius.
    else:
        return None  #devuelve None para indicar que no se puede realizar la conversión.

Temperatura = float(input("Ingrese la temperatura: "))
tipo = input("Ingrese el tipo de temperatura (Celsius, Fahrenheit): ")
resultado = convertir_temperatura(Temperatura, tipo)
if resultado is not None: #is not None evalua si el resultado de la conversión es válido (es decir, si se pudo realizar la conversión correctamente). Si el resultado no es None, significa que la conversión fue exitosa y se puede mostrar el resultado al usuario.
    print(f"La temperatura convertida es: {resultado}")
else:
    print("Tipo de temperatura no válido.")

#Ejercicio 9...
print("Menú de operaciones")
def mostrar_menu():
    while True:
        print("\nMenú de operaciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Salir")
        
        opcion = int(input("Seleccione una opción (1, 2 o 3): "))
        
        if opcion == 1: #if opcion == 1 evalua si el usuario seleccionó la opción 1 del menú, que corresponde a la operación de suma. Si es así, se solicita al usuario que ingrese dos números y se realiza la suma de esos números, mostrando el resultado en pantalla.
            n1 = float(input("Ingrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))
            print(f"La suma es: {n1 + n2}")
        elif opcion == 2:
            n1 = float(input("Ingrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))
            print(f"La resta es: {n1 - n2}")
        elif opcion == 3:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción correcta.")

#Ejercicio 10...
print("Gestión de libros")
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True #disponible es un atributo que indica si el libro está disponible para prestar o no. Se inicializa como True, lo que significa que el libro está disponible al momento de crearlo.

    def prestar(self):
        if self.disponible:
            self.disponible = False #self.disponible = False cambia el estado del libro a no disponible, indicando que ha sido prestado. Esto evita que el libro pueda ser prestado nuevamente hasta que sea devuelto.
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para prestar.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True #self.disponible = True cambia el estado del libro a disponible, indicando que ha sido devuelto.
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def estado(self):
        estado_libro = "disponible" if self.disponible else "no disponible" #Evalua si el libro está disponible o no y asigna el valor correspondiente a la variable estado_libro. Si self.disponible es True, significa que el libro está disponible y se asigna "disponible" a estado_libro. Si self.disponible es False, significa que el libro no está disponible y se asigna "no disponible" a estado_libro.
        print(f"El libro '{self.titulo}' de {self.autor} está {estado_libro}.")

#Solicitar 3 libros al usuario
libros = [] #Crear una lista vacía llamada libros para almacenar los objetos de la clase Libro que se crearán a partir de los datos ingresados por el usuario.
for i in range(3):
    titulo = input(f"Ingrese el título del libro {i + 1}: ") #i+1 para que empiece desde 1 y no desde 0
    autor = input(f"Ingrese el autor del libro {i + 1}: ")
    libros.append(Libro(titulo, autor)) #Crea un nuevo objeto de la clase Libro utilizando los datos ingresados por el usuario (título y autor) y lo agrega a la lista libros. Esto permite almacenar múltiples libros en la lista para su posterior gestión.

#Pretar, devolver y mostrar estado de los libros
libros[0].prestar()  #Presta el primer libro
libros[1].devolver()  #Devurelve el segundo libro (aunque ya está disponible, para mostrar el mensaje)
# Mostrar el estado final de los libros
for libro in libros:
    libro.estado()

#Ejercicio 11...
print("Gestión de vehículos")
class Vehiculo:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self, incremento): #self, incremento son los parámetros que recibe el método acelerar. self hace referencia a la instancia actual del objeto Vehiculo, mientras que incremento es el valor que se sumará a la velocidad actual del vehículo.
        self.velocidad += incremento #+= operador de asignación que incrementa el valor de self.velocidad en la cantidad especificada por incremento. Esto significa que la velocidad actual del vehículo se incrementará en el valor proporcionado.
        print(f"El vehículo {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")

    def frenar(self, decremento):
        self.velocidad -= decremento #-= operador de asignación que decrementa el valor de self.velocidad en la cantidad especificada por decremento. Esto significa que la velocidad actual del vehículo se reducirá en el valor proporcionado.
        if self.velocidad < 0: 
            self.velocidad = 0
        print(f"El vehículo {self.marca} {self.modelo} ha frenado a {self.velocidad} km/h.")

# Crear dos vehículos
vehiculos = [] 
for i in range(2):
    marca = input(f"Ingrese la marca del vehículo {i + 1}: ")
    modelo = input(f"Ingrese el modelo del vehículo {i + 1}: ")

    velocidad = float(input(f"Ingrese la velocidad inicial del vehículo {i + 1} (km/h): "))
    vehiculos.append(Vehiculo(marca, modelo, velocidad))
#Acelerar y frenar viarias veces cada uno y mostrar la velocidad final
for vehiculo in vehiculos:
    for _ in range(3):  # Acelerar 3 veces
        incremento = float(input(f"Ingrese el incremento de velocidad para {vehiculo.marca} {vehiculo.modelo}: "))
        vehiculo.acelerar(incremento)

    for _ in range(2):  # Frenar 2 veces
        decremento = float(input(f"Ingrese el decremento de velocidad para {vehiculo.marca} {vehiculo.modelo}: "))
        vehiculo.frenar(decremento)
#Velocidad final de cada vehículo
for vehiculo in vehiculos:
    print(f"La velocidad final del vehículo {vehiculo.marca} {vehiculo.modelo} es {vehiculo.velocidad} km/h.")

#Ejercicio 12...
print("Gestión de productos")
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}.")
        else:
            print(f"No hay suficiente stock de {self.nombre}. Stock disponible: {self.stock}.")
#Crear tres productos
productos = []
for i in range(3):
    nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    stock = int(input(f"Ingrese el stock del producto {i + 1}: "))
    productos.append(Producto(nombre, precio, stock))
#Simular ventas de cada producto
for producto in productos:
    cantidad = int(input(f"Ingrese la cantidad a vender del producto {producto.nombre}: "))
    producto.vender(cantidad)
#Stock final de cada producto
for producto in productos:
    print(f"Stock final del producto {producto.nombre}: {producto.stock}.")

#Ejercicio 13...
print("Gestión de estudiantes y notas")
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota {nota} agregada para el estudiante {self.nombre}.")

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
#crear dos estudiantes
estudiantes = []
for i in range(2):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    estudiantes.append(Estudiante(nombre))
#Mostrar promedio de cada estudiante
for estudiante in estudiantes:
    while True:
        try:
            nota = float(input(f"Ingrese una nota para {estudiante.nombre} (o escriba 'fin' para terminar): "))
            estudiante.agregar_nota(nota)
        except ValueError:
            break  # Salir del bucle si el usuario escribe algo que no sea un número
    print(f"El promedio de notas de {estudiante.nombre} es: {estudiante.promedio()}")

#Ejercicio 14...
print("Gestión de tareas")
class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.completada = False

    def completar(self):
        self.completada = True
        print(f"La tarea '{self.nombre}' ha sido completada.")

    def estado(self):
        estado_tarea = "completada" if self.completada else "pendiente"
        return f"Tarea: {self.nombre}, Estado: {estado_tarea}"
    
class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea.nombre}' agregada al gestor.")

    def mostrar_tareas(self):
        for tarea in self.tareas:
            print(tarea.estado())
#Crear cinco tareas
gestor = GestorTareas() #Creación de objeto de la clase Gestor Tareas, guardada en variable gestor.
for i in range(5): #Bucle en el que indico que se repita 5 veces.
    nombre = input(f"Ingrese el nombre de la tarea {i + 1}: ")
    tarea = Tarea(nombre)
    gestor.agregar_tarea(tarea) #Llama al método que esta dentro de gestor que se llama agregar tarea y le pasa el objeto tarea que se crea.

#Completar dos tareas
for i in range(2):
    nombre = input(f"Ingrese el nombre de la tarea a completar {i + 1}: ")
    for tarea in gestor.tareas:
        if tarea.nombre == nombre: #== es un operador de comparación que sirve para comprobar si dos valores o variables son iguales.
            tarea.completar()
            break

# Estado de todas las tareas
print("\nEstado de todas las tareas:")
gestor.mostrar_tareas()
#Ejercicio 15...
print("Gestión de productos")
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}"

#almacenar los productos en una lista
productos = []

#Solicitar al usuario que ingrese varios productos
while True:
    nombre = input("Ingrese el nombre del producto (o escriba 'fin' para terminar): ")
    if nombre.lower() == 'fin': #.lower() función que convierte todas las letras a minúsculas.
        break
    precio = float(input(f"Ingrese el precio del producto '{nombre}': "))
    stock = int(input(f"Ingrese el stock del producto '{nombre}': "))
    productos.append(Producto(nombre, precio, stock)) #.append metodo que añade un elemento al final de un lista ya existente.

#Mostrar un reporte final con todos los productos registrados
print("\nReporte final de productos registrados:")
for producto in productos:
    print(producto.mostrar_info())