from alumno import Alumno
from curso import Curso
from universidad import Universidad

#Creamos al alumno
objeto_alumno = Alumno("Juan Lopez", "AL-001")

#Creamos cursos
objeto_curso1 = Curso("Programacion Orientada a Objetos", "C-001")
objeto_curso2 = Curso("Fisica", "C-002")
objeto_curso3 = Curso("Calculo Diferencial", "C-003")
objeto_curso4 = Curso("Algoritmos y Estructuras de Datos", "C-004")


#Agregamos cursos a los alumnos
objeto_alumno.agregar_curso(objeto_curso1)
objeto_alumno.agregar_curso(objeto_curso2)
objeto_alumno.agregar_curso(objeto_curso3)
objeto_alumno.agregar_curso(objeto_curso4)

#Agregamos universidad a los alumnos

objeto_alumno.mostrar_cursos()

#Creamos universidad
objeto_universidad1 = Universidad("UPANA")
objeto_universidad1.agregar_alumnos(objeto_alumno)
objeto_universidad1.mostrar_universidad()
