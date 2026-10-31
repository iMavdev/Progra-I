class Usuario:
    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo
        self.__cuenta = None

@property
def nombre(self):
    return self.__nombre

@nombre.setter
def nombre(self, nuevo_nombre):
    self.__nombre = nuevo_nombre  

@property
def correo(self):
    return self.__correo

@correo.setter
def correo(self, nuevo_correo):
    self.__correo = nuevo_correo

@property
def cuenta(self):
    return self.__cuenta

@cuenta.setter
def cuenta(self, nueva_cuenta):
    self.__cuenta = nueva_cuenta

def depositar(self,cantidad):
    if self.__cuenta is not None:
        self.__cuenta.depositar(cantidad)
    else:
        print("El usuario no tiene una cuenta asociada.")

def retirar(self,cantidad):
    if self.__cuenta is not None:
        self.__cuenta.retirar(cantidad)
    else:
        print("El usuario no tiene una cuenta asociada.")
