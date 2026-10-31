from marca import Marca
from producto import Producto


#Creo las marcas
objeto_marca = Marca("Electrónico", "MSI")
objeto_marca2 = Marca ("Electrónico", "Logitech")


#Creo productos para la marca MSI
objeto_producto1 = Producto("Laptop", 1500)
objeto_producto2 = Producto("Tarjeta gráfica", 5000)
objeto_producto3 = Producto("Teclado", 100)


#Creo productos para la marca Logitech
objeto_producto4 = Producto("Mousepad", 120)
objeto_producto5 = Producto("Mouse", 200)
objeto_producto6 = Producto("Auriculares", 350)

#Agrego producto a la marca MSI
objeto_marca.agregar_producto(objeto_producto1)
objeto_marca.agregar_producto(objeto_producto2)
objeto_marca.agregar_producto(objeto_producto3)


#Agrego producto a la marca Logitech
objeto_marca2.agregar_producto(objeto_producto4)
objeto_marca2.agregar_producto(objeto_producto5)
objeto_marca2.agregar_producto(objeto_producto6)


#Muestro en pantalla los productos que pertenece a la marca MSI
objeto_marca.mostrar_productos()

#Muestro en pantalla los productos que pertececen a la marca Logitech
objeto_marca2.mostrar_productos()