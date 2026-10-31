class computer:
    def __init__(self, marca, ram):
        self.marca = marca
        self.ram = ram

    def informacion (self):
        print (f"La marca de la computadora es: {self.marca}, memoria RAM {self.ram} GB")

def validar_marca ():
    marca_valida=input("Ingrese la marca de la Computadora").strip() #.strip() elimina espacios al inicio y al fin

    while marca_valida == "" or not marca_valida.replace(" ","").isalpha():
        print ("Marca invalida, ingrese nuevamente")
        marca_valida=input("Ingrese la marca de la Computadora: ")
    return marca_valida

def validar_ram ():
    ram_valida=input ("Ingrese la cantidad de memoria RAM").strip()

    while ram_valida == "" or not ram_valida.replace(" ","").isdigit():
        print("RAM inválida, ingrese nuevamente")
        ram_valida=input("Ingrese la cantidad de memoria RAM: ")
    return ram_valida

marca = validar_marca ()
ram = validar_ram ()

pc_objeto = computer (marca,ram)
pc_objeto.informacion ()