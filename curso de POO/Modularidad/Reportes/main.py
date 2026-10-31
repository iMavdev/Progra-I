from calculos import subtotal, calcular_impuestos, total
from reportes import mostrar_productos, mostrar_ventas

# Variables locales dentro del main.py
nombre_producto = "Camiseta"
precio_producto = 20.0
cantidad_producto = 3

# Calcular subtotal
# Variables locales dentro del main.py
subtotal_producto = subtotal(precio_producto, cantidad_producto)

# Calcular impuestos
# Variables locales dentro del main.py
impuestos_producto= calcular_impuestos(subtotal_producto,0.1)

#Calcular Total
# Variables locales dentro del main.py
total_producto = total(subtotal_producto, impuestos_producto)

# Mostrar información
mostrar_productos(nombre_producto, precio_producto, cantidad_producto) # Variables locales dentro del main.py
mostrar_ventas(subtotal_producto, impuestos_producto, total_producto) # Variables locales dentro del main.py