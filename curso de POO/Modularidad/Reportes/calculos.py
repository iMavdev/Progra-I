def subtotal(precio, cantidad):
    return precio * cantidad

def calcular_impuestos(subtotal, tasa_impuesto):
    return subtotal * tasa_impuesto

def total(subtotal, impuestos):
    return subtotal + impuestos

