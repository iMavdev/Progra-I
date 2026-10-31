class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_name):

        if nuevo_name  == "" or not nuevo_name.replace(" ", "").isalpha():
            print("Nombre inválido, ingrese de nuevo.")
        else:
            self.__nombre = nuevo_name

name = Persona("Andrea")
print(name.nombre)

nuevo_name = input("Ingrese nuevo nombre: ")

while nuevo_name == "" or not nuevo_name.replace(" ", "").isalpha():
    print("Nombre inválido, ingrese de nuevo.")
    nuevo_name = input("Ingrese nuevo nombre: ")


name.nombre = nuevo_name
print(f"El nombre ingresado es: {nuevo_name}")
