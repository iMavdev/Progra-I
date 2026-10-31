class Libro:
    def __init__(self, codigo, titulo, autor):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    def mostrar_informacion(self):
        print(f"Código del libro: {self.__codigo} Título del libro: {self.__titulo} Autor del libro: {self.__autor} ")
        