from alumno import Alumno
from curso import Curso


obj_alumno1 = Alumno("Juan Pérez", "2026001")
obj_alumno2 = Alumno("María López", "2026002")


obj_curso1 = Curso("Programación Orientada a Objetos", "POO101")
obj_curso2 = Curso("Física", "FIS101")


print ("inscribiendo cursos par el alumno 1:")
obj_alumno1.agregar_curso(obj_curso1)
obj_alumno1.agregar_curso(obj_curso2)


print("\nInscribiendo cursos para el alumno 2:")
obj_alumno2.agregar_curso(obj_curso1)


print("\nMostrando información del alumno 1:")
obj_alumno1.mostrar_informacion()


print("\nMostrando información del alumno 2:")
obj_alumno2.mostrar_informacion()

print("\nBuscando curso del alumno 1:")
curso_encontrado = obj_alumno1.buscar_curso(obj_curso1.codigo)

if curso_encontrado:
    print(f"El alumno {obj_alumno1.nombre} está inscrito en el curso: {curso_encontrado.nombre}")
else:
    print(f"El alumno {obj_alumno1.nombre} no está inscrito en el curso con código {obj_curso1.codigo}.")

print ("\nIntentando agregar curso repetido")
obj_alumno1.agregar_curso(obj_curso1)

print("\nEliminando curso del alumno 1:")
obj_alumno1.eliminar_curso(obj_curso1.codigo)