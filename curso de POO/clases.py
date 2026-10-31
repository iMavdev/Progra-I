class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def hablar(self):
        print(f"hola mi nombre es {self.nombre} {self.apellido} {self.edad}")
    
    def longitud(self):
        return len(self.nombre) + len(self.apellido)

P1 = Persona("juan", "perez", 30)
P1.hablar()
print(f"la longitud del nombre y apellido es: {P1.longitud()}")

if P1.longitud() % 2 == 0:
    print("la longitud es par")
else:
    print("la longitud es impar")
