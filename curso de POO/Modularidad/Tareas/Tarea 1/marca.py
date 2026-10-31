class Marca:
    def __init__(self, tipo, nombre,):
        self.__tipo = tipo
        self.__nombre = nombre
        self.__productos = []


    def agregar_producto(self, producto):
        self.__productos.append(producto)


    def mostrar_productos(self):
        print(f"\033[1mProductos de la marca {self.__nombre}\033[0m")
        print(f"Tipo: {self.__tipo}")
        print(f"_____________________________________")

        for producto in self.__productos:
            producto.mostrar()