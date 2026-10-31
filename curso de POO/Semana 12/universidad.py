class Universidad:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__alumnos = []
    

    @property
    def nombre(self):
        return self.__nombre

    def agregar_alumnos(self, alumno):
           self.__alumnos.append(alumno)

    def mostrar_universidad (self):
        print(f"Universidad: {self.__nombre}")

        for alumno in self.__alumnos:
            alumno.mostrar_alumnos()

   