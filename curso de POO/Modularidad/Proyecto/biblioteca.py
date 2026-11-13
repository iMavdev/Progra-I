from datetime import datetime
from prestamo import Prestamo
class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []

    #Métodos para libros
    def agregar_libro(self, libro):
        codigo = libro.consultar_codigo().strip().upper()

        if self.buscar_libro(codigo):
            print(f"Ya existe un libro con el código {codigo}.")
            print ("------------------------------------------")
            return

        self.__libros.append(libro)
        print(f"Libro con código {codigo} registrado correctamente.")
        print(f"Fecha y hora de registro: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print ("-----------------------------------------------")

    def buscar_libro(self, codigo, mostrar=False):
        codigo = codigo.strip().upper()
        for libro in self.__libros:
            if libro.consultar_codigo().strip().upper() == codigo:
                if mostrar:
                    libro.mostrar_informacion_libro()
                    print ("--------------------------------")
                return libro
        if mostrar:
            print(f"No se encontró un libro con el código {codigo}.")
            print ("-----------------------------------------------")
        return None

    def eliminar_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro:
            self.__libros.remove(libro)
            print (f"Libro '{libro.titulo()}' eliminado de la biblioteca.")
            print ("-----------------------------------------------------")
        else:
            print (f"Libro con código {codigo} no encontrado en la biblioteca.")
            print ("----------------------------------------------------------")
    
    def mostrar_libros(self):
        if len(self.__libros) == 0:
            print("No hay libros registrados.")
            print("--------------------------")
            return
        
        print("=== Libros Registrados ===")
        for libro in self.__libros:
                libro.mostrar_informacion_libro()
                print("-------------------------------")

    #Métodos para usuarios
    def agregar_usuario(self, usuario):
        if self.buscar_usuario(usuario.consultar_carnet()):
            print(f"Ya existe un usuario con el carnet {usuario.consultar_carnet()}.")
            print ("----------------------------------------------------------------")

            return
        self.__usuarios.append(usuario)
        print (f"Usuario con carnet {usuario.consultar_carnet()} registrado correctamente.")
        print(f"Fecha y hora de registro: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print ("-------------------------------------------------")

    def buscar_usuario(self, carnet, mostrar=False):
        carnet = carnet.strip().upper()
        for usuario in self.__usuarios:
            if usuario.consultar_carnet().strip().upper() == carnet:
                if mostrar:
                    usuario.mostrar_informacion_usuario()
                    print("------------------------------")
                return usuario
        if mostrar:
            print(f"No se encontró un usuario con el carnet {carnet}.")
            print("-----------------------------------------")
        return None

    def mostrar_usuarios(self):
        if not self.__usuarios:
            print("No hay usuarios registrados.")
            print ("---------------------------")
        else:
            print("=== Usuarios Registrados ===")
            for usuario in self.__usuarios:
                usuario.mostrar_informacion_usuario()
                print("------------------------------")

    #Métodos para préstamos
    def realizar_prestamo(self, usuario, libro):
        if usuario is None:
            print ("EL usuario no existe.")
            print ("---------------------")
        elif libro is None:
            print ("El libro no existe en biblioteca.")
            print ("---------------------------------")
        elif libro.consultar_estado() == "disponible":
            libro.cambiar_estado("prestado")
            nuevo_prestamo = Prestamo(usuario, libro)
            self.__prestamos.append(nuevo_prestamo)
            print("Préstamo realizado con éxito.")
            print(f"Fecha y hora del préstamo: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print("----------------------------------------------")
        else:
            print("El libro no está disponible para préstamo.")
            print("------------------------------------------")

    def devolver_libro(self, usuario, libro):
        prestamo = None
        for prestamo_libro in self.__prestamos:
            if prestamo_libro.consultar_usuario() == usuario and prestamo_libro.consultar_libro() == libro:
                prestamo = prestamo_libro
                break

        if prestamo:
            libro.cambiar_estado("disponible")
            self.__prestamos.remove(prestamo)
            print("Libro devuelto con éxito.")
            print(f"Fecha y hora de devolución: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print("-----------------------------------------------")
        else:
            print("No se encontró un préstamo correspondiente para este usuario y libro.")
            print("---------------------------------------------------------------------")

    def mostrar_prestamos(self):
        if not self.__prestamos:
            print("No hay préstamos registrados.")
            print ("----------------------------")
        else:
            print("=== Préstamos Registrados ===")
            for prestamo in self.__prestamos:
                prestamo.mostrar_informacion_prestamo()
                