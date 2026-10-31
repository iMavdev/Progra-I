from cliente import Cliente
from producto import Producto
from venta import Venta


clientes = []
productos = []
ventas = []


def buscar_cliente(codigo):
	for cliente in clientes:
		if cliente.codigo == codigo:
			return cliente
	return None


def buscar_producto(codigo):
	for producto in productos:
		if producto.codigo == codigo:
			return producto
	return None


def registrar_cliente():
	codigo = input("Codigo del cliente: ")

	if buscar_cliente(codigo) is not None:
		print("Ya existe un cliente con ese codigo.")
		return

	nombre = input("Nombre del cliente: ")
	correo = input("Correo del cliente: ")
	
	cliente = Cliente(codigo, nombre, correo)
	clientes.append(cliente)
	print("Cliente registrado correctamente.")


def registrar_producto():
	codigo = input("Codigo del producto: ")

	if buscar_producto(codigo) is not None:
		print("Ya existe un producto con ese codigo.")
		return

	nombre = input("Nombre del producto: ")
	precio = float(input("Precio del producto: "))
	stock = int(input("Stock del producto: "))

	if precio < 0 or stock < 0:
		print("El precio y el stock no pueden ser negativos.")
		return

	
	producto = Producto(codigo, nombre, precio, stock)
	productos.append(producto)
	print("Producto registrado correctamente.")


def mostrar_clientes():
	if len(clientes) == 0:
		print("No hay clientes registrados.")
		return

	for cliente in clientes:
		print(f"Codigo: {cliente.codigo} | Nombre: {cliente.nombre} | Correo: {cliente.correo}")


def mostrar_productos():
	if len(productos) == 0:
		print("No hay productos registrados.")
		return

	for producto in productos:
		print(f"Codigo: {producto.codigo} | Nombre: {producto.nombre} | Precio: Q{producto.precio} | Stock: {producto.stock}")


def crear_venta():
	codigo_cliente = input("Codigo del cliente: ")
	cliente = buscar_cliente(codigo_cliente)

	if cliente is None:
		print("El cliente no existe.")
		return


	venta = Venta()

	venta.relacioncliente = cliente

	while True:
		codigo_producto = input("Codigo del producto (0 para terminar): ")

		if codigo_producto == "0":
			break

		producto = buscar_producto(codigo_producto)

		if producto is None:
			print("El producto no existe.")
			continue

		cantidad = int(input("Cantidad: "))

		if cantidad <= 0:
			print("La cantidad debe ser mayor que cero.")
			continue

		if cantidad > producto.stock:
			print(f"No hay suficiente stock. Stock disponible: {producto.stock}")
			continue


		venta.agregar_producto(producto, cantidad)

	if len(venta.productos) == 0:
		print("La venta no tiene productos y no fue registrada.")
		return

	ventas.append(venta)
	print("Venta registrada correctamente.")
	
	venta.mostrar_detalle()


def mostrar_ventas():
	if len(ventas) == 0:
		print("No hay ventas registradas.")
		return

	numero_venta = 1
	for venta in ventas:
		print("Venta", numero_venta)

		venta.mostrar_detalle()
		numero_venta = numero_venta + 1



#Menu principal
def mostrar_menu():
	print("\n--- MENU ---")
	print("1. Registrar cliente")
	print("2. Registrar producto")
	print("3. Mostrar clientes")
	print("4. Mostrar productos")
	print("5. Crear venta")
	print("6. Mostrar ventas")
	print("7. Salir")


opcion = ""
while opcion != "7":
	mostrar_menu()
	opcion = input("Seleccione una opcion: ")

	if opcion == "1":
		registrar_cliente()
	elif opcion == "2":
		registrar_producto()
	elif opcion == "3":
		mostrar_clientes()
	elif opcion == "4":
		mostrar_productos()
	elif opcion == "5":
		crear_venta()
	elif opcion == "6":
		mostrar_ventas()
	elif opcion == "7":
		print("Programa finalizado.")
	else:
		print("Opcion no valida.")
