class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__relacioncuenta = None
        self.__relaciontc = None

    @property
    def nombre(self):
        return self.__nombre

    @property
    def relacioncuenta(self):
        return self.__relacioncuenta

    @relacioncuenta.setter
    def relacioncuenta(self, nueva_cuenta):
        self.__relacioncuenta = nueva_cuenta

    @property
    def relaciontc(self):
        return self.__relaciontc

    @relaciontc.setter
    def relaciontc(self, nueva_tc):
        self.__relaciontc = nueva_tc

      