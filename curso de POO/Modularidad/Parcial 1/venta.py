class Venta:
    def __init__(self):
        self.__relacioncliente = None
        self.__productos = []

    @property
    def relacioncliente(self):
        return self.__relacioncliente

    @relacioncliente.setter
    def relacioncliente(self, cliente):
        self.__relacioncliente = cliente

    @property
    def productos(self):
        return self.__productos

    @property
    def total(self):
        total = 0

        for venta in self.__productos:
            producto = venta[0]
            cantidad = venta[1]
            total = total + producto.precio * cantidad

        return total

    def agregar_producto(self, producto, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        if cantidad > producto.stock:
            print(f"No hay suficiente stock de {producto.nombre}.")
            return

        producto.stock = -cantidad
        self.__productos.append((producto, cantidad))
        print(f"Producto agregado: {producto.nombre} x{cantidad}")

    def mostrar_detalle(self):
        print(f"Cliente: {self.__relacioncliente.nombre}")
        print("Detalle de la venta:")

        for venta in self.__productos:
            producto = venta[0]
            cantidad = venta[1]
            subtotal = producto.precio * cantidad
            print(f"- {producto.nombre} x{cantidad}: Q{subtotal}")

        print(f"Total: Q{self.total}")
    