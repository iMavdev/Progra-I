class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre


    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            print(f"Precio no puede ser negativo. Se mantiene el actual: {self.__precio}")
        else:
            self.__precio = nuevo_precio
            print(f"Precio actualizado. Nuevo precio: {self.__precio}")


    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, nuevo_stock):
        stock_actualizado = self.__stock + nuevo_stock
        if stock_actualizado < 0:
            print(f"Stock no puede ser negativo. Se mantiene el actual: {self.__stock}")
        elif nuevo_stock == 0:
            print(f"El stock se mantiene en: {self.__stock}")
        else:
            self.__stock = stock_actualizado
            print(f"Stock actualizado. Nuevo stock: {self.__stock}")       