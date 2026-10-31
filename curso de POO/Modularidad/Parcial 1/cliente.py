class Cliente:
    def __init__(self, codigo, nombre, correo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__correo = correo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo