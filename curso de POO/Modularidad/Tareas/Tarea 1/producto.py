class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio


    @property
    def nombre(self):
        return self.__nombre


    @property
    def precio(self):
        return self.__precio


    def mostrar(self):
        print(f"Producto: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"_____________________________________")