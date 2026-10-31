class Biblioteca:
    def __init__(self, libros):
        self.__libros = []


    def verificar_libro(self, codigo):
        for libro in self.__libros:
            if libro.codigo == codigo:
                return True
        return False


    def agregar_libro(self, libro):
        if self.verificar_libro(libro.codigo):
            print(f"El libro con código {libro.codigo} ya está registrado en la biblioteca.")
            return

        self.__libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")


    def buscar_libro(self, codigo):
        for libro in self.__libros:
            if libro.codigo == codigo:
                return libro
        return None


    def mostrar_libros(self):
        if len(self.__libros) == 0:
            print("No hay libros registrados en la biblioteca.")
            return

        print("Libros registrados en la biblioteca:")
        for libro in self.__libros:
            libro.mostrar_informacion()


    def eliminar_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro:
            self.__libros.remove(libro)
            print(f"Libro '{libro.titulo}' eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con código {codigo} en la biblioteca.")