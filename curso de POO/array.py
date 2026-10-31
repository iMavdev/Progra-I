#Clase
class perro:
    def __init__(self, nombre, raza):
        #Atributos
        self.nombre_perro=nombre
        self.raza_perro=raza
    #Método
    def informacion (self):
        print(f"El nombre del perro es {self.nombre_perro} de raza {self.raza_perro}")

Perros = [] #Variable tipo vector (array)
#Solicitar datos
cantidad = int (input("Cuantos perross quiere ingresar"))

for i in range (cantidad):
    print (f"\nPerro No {i+1}") #{i+1} contador en el que dice que empiece en 1 y no en 0
    nombre = input ("Nombre: ")
    raza = input ("Raza: ")

    #Construir el ojeto e introducirlo dentro de variable y luego se introduce dentro de array
    p=perro(nombre,raza)

    #El objeto p lo ingresamos al array Perros = [P] Consejo de Ing: Cyberseguridad, IA y Ciencia de Datos 
    Perros.append(p) #Append adicionar algo a Perros

#Se hacen listados
print("\nLista de perros registrados ")
for p in Perros:
    p.informacion


for i in range (len [p]):
    print (f"\nPerro No {i+1}")
    p.informacion()