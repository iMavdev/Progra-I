class Prestamo:
    def __init__(self, usuario, libro):
        self.__usuario = usuario
        self.__libro = libro

    def mostrar_informacion_prestamo(self):
        print("Información del préstamo:")
        print("Datos del usuario:")
        print("-------------------------")
        self.__usuario.mostrar_informacion_usuario()
        print("-------------------------")
        print("Datos del libro: ")
        print("-------------------------")
        self.__libro.mostrar_informacion_libro()
        print("-------------------------")

    def consultar_usuario(self):
        return self.__usuario

    def consultar_libro(self):
        return self.__libro
    
