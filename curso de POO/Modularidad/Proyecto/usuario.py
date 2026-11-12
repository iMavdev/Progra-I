class Usuario:
    def __init__(self, carnet, nombre, correo):
        self.__carnet = carnet
        self.__nombre = nombre
        self.__correo = correo

    def mostrar_informacion_usuario(self):
        print(f"Carnet: {self.__carnet}")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")

    def consultar_carnet(self):
        return self.__carnet

    def consultar_nombre(self):
        return self.__nombre

    