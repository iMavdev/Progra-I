class Libro:
    def __init__(self, codigo, titulo, autor, yearpublication, estado):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__yearpublication = yearpublication
        self.__estado = estado

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def yearpublication(self):
        return self.__yearpublication
    
    @property
    def estado(self):
        return self.__estado

    def mostrar_informacion_libro(self):
        print(f"Código: {self.__codigo}")
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Año de publicación: {self.__yearpublication}")
        print(f"Estado: {self.__estado}")

    def cambiar_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def consultar_estado(self):
        return self.__estado

    def consultar_codigo(self):
        return self.__codigo
    