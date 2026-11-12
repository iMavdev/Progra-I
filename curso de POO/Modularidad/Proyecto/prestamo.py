class Prestamo:
    def __init__(self, usuario, libro):
        self.__usuario = usuario
        self.__libro = libro

    def mostrar_informacion_prestamo(self):
        print("Información del préstamo:")
        print("Datos del usuario:")
        self.__usuario.mostrar_informacion_usuario()
        print("Datos del libro: ")
        self.__libro.mostrar_informacion_libro()

    def consultar_usuario(self):
        return self.__usuario

    def consultar_libro(self):
        return self.__libro
    
