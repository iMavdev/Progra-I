class Auto_clase:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacion (self):
        print (f"el auto es de marca {self.marca} modelo {self.modelo}")

def validar_marca (): #Validar Letras
    marca_valida=input("Ingrese la marca del auto ").strip() #.strip () elimina espacios al inicio y al fin

    #(== "") es nada o vacío, cuando el usuario da un enter  sin ingresar un dato
    while marca_valida == "" or not marca_valida.replace(" ", "").isalpha(): #.replace " ", "" reemplace todos los espacios, .isalpha Si tiene solo números o letras valida o devuelve un verdadero o un falso
        print ("Marca invalida, ingrese nuevamente")
        marca_valida=input("Ingrese la marca del auto")
    return marca_valida

def validar_modelo (): #Validar Números
    modelo_valido=input ("Ingrese el modelo del auto ").strip()#.strip () elimina espacios al inicio y al fin

    #While busca que todo sea verdadero
    while modelo_valido == "" or not modelo_valido.replace(" ","").isdigit():
        print("Modelo inválido, ingrese nuevamente")
        modelo_valido=input("Ingrese el modelo del auto: ")
    return modelo_valido


marca = validar_marca ()
modelo = validar_modelo ()

auto_objeto = Auto_clase (marca,modelo)
auto_objeto.informacion ()