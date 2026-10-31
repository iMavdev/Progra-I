class Alumno:
    def __init__(self, nombre, carnet):
        self.__nombre = nombre
        self.__carnet = carnet
        self.__cursos = []


    @property
    def nombre(self):
        return self.__nombre


    @property
    def carnet(self):
        return self.__carnet


    def verificar_curso(self, codigo_curso):
        for curso_buscar in self.__cursos:  #curso_buscar es una variable que representa cada curso en la lista de cursos del alumno
            if curso_buscar.codigo == codigo_curso: #Va a buscar al ojeto que heredo todo lo de tiene la clase Curso
                return True
        return False


    def agregar_curso(self, curso):
        if self.verificar_curso(curso.codigo):
            print(f"El alumno ya está inscrito en el curso {curso.nombre}.")
            return


        self.__cursos.append(curso)
        print(f"Curso {curso.nombre} agregado al alumno {self.__nombre}.")

    def buscar_curso(self, codigo_curso):
        for curso in self.__cursos: #curso es una variable
            if curso.codigo == codigo_curso: # Busca el curso por su código
                return curso
        return None

    def eliminar_curso(self, codigo_curso):
        curso = self.buscar_curso(codigo_curso)
        if curso:
            self.__cursos.remove(curso)
            print(f"Curso {curso.nombre} eliminado del alumno {self.__nombre}.")
        else:
            print(f"No se encontró el curso con código {codigo_curso} para el alumno {self.__nombre}.")

    
    def mostrar_informacion(self):
        if len (self.__cursos) == 0:
            print(f"El alumno {self.__nombre} no está inscrito en ningún curso.")
            return

        print(f"Información del alumno {self.__nombre}:")
        for curso in self.__cursos:
            curso._mostrar_informacion()

