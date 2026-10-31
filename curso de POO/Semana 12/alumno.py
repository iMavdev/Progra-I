class Alumno:
    def __init__(self, nombre, id):
        self.__nombre = nombre
        self.__id = id
        self.__cursos = []

    def agregar_curso(self, curso):
        self.__cursos.append(curso)

    def mostrar_cursos(self):
        print(f"Cursos del alumno {self.__nombre}")
        print(f"ID: {self.__id}")

        for curso in self.__cursos:
            curso.mostrar() #trae el metodo que se llama mostrar del formuulario curso de la Clase Curso.

    def mostrar_alumnos(self):
        print(f"Alumno: {self.__nombre}")
        print(f"ID: {self.__id}")
         
