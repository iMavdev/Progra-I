class universidad:
    def __init__(self, nombre, campus, ubicacion):
        #Atributos
        self.nombre = nombre
        self.campus = campus
        self.ubicacion = ubicacion

    def bienvenida (self): #Método
        print (f"Bienvenido a la Universidad {self.nombre}, Campus: {self.campus}, Ubicado en: {self.ubicacion}")

alumno1=universidad ("Panamericana", "Cobán", "Zona 8")
alumno1.bienvenida()

# Clase Universidad solicitando datos
class universidad:
    def __init__(self, nombre, campus, ubicacion):
        #Atributos
        self.nombre = nombre
        self.campus = campus
        self.ubicacion = ubicacion

    def bienvenida (self): #Método
        print (f"Bienvenido a la Universidad {self.nombre}, Campus: {self.campus}, Ubicado en: {self.ubicacion}")

name=str(input("Ingrese el nombre de la Universidad: "))
camp=str(input("Ingrese el Campus: "))
ubi=str(input("Ingrese la dirección de la Universidad: "))

alumno1=universidad (name,camp,ubi)
alumno1.bienvenida()


# Clase Suma
class suma:
    def __init__(self, n1,n2):
        r=n1+n2 #r->resultado
        #Atributo
        self.resultado = r

    def operacion(self,n3): #Método
        return self.resultado + n3

datos1 = suma (50,100) #Llama a la Clase
print (f"El resultado es: {datos1.operacion (50)}") #Llama al método


# Clase Suma Solicitando Datos
class suma:
    def __init__(self, n1,n2):
        r=n1+n2 #r->resultado
        #Atributo
        self.resultado = r

    def operacion(self,n3): #Método
        return self.resultado + n3

n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))

datos1 = suma (n1,n2) #Llama a la Clase
print (f"El resultado es: {datos1.operacion (50)}") #Llama al método