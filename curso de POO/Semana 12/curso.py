 #Llaves en DB el ID puede ser autonumerico pero no es lo escencial, se debe de usar GUID(16 caracteres en adelante).
class Curso:
    def __init__(self,nombre, codigo): #el orden que manda al momento de llamar.
        self.__codigo=codigo #__ para encapsular el atributo, no se puede acceder desde fuera de la clase.
        self.__nombre=nombre

    @property 
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    def mostrar (self):
        print(f"{self.__codigo} - {self.__nombre}")
        