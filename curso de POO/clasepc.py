class computadora: 
    def __init__(self, marca, generacion): # lo que esta entre las comas son variables e __init__ es constructor
        #self.marca es atributo
        self.marca = marca
        #self.generación es atributo
        self.generación = generacion

    def promocion (self): # Metodo
        print (f"Equipos en promoción {self.marca} generación {self.generación}")

compu1=computadora("MSI", 13) #Atributo
compu1.promocion() # Método
