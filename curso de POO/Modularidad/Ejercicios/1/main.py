from curso import Curso
from alumno import Alumno
from universidad import Universidad

#Objetos
alumno1 = Alumno("Juan")
curso1 = Curso("Python") 
curso2 = Curso("POO")

#Primera relación entre Alumno y Curso
alumno1.relacioncurso = curso1

print(f"El Alumno {alumno1.nombre} esta inscrito en el Curso {alumno1.relacioncurso.nombre} posee una nota de {alumno1.relacioncurso.nota}.")

#Primera Nota del curso 1 del Alumno en el Curso
alumno1.relacioncurso.nota = 10

print (f"El Alumno {alumno1.nombre} esta inscrito en el Curso {alumno1.relacioncurso.nombre} posee una nota de {alumno1.relacioncurso.nota}.")

#Segunda relación entre Alumno y Curso
alumno1.relacioncurso2 = curso2

print(f"El Alumno {alumno1.nombre} esta inscrito en el Curso {alumno1.relacioncurso2.nombre} posee una nota de {alumno1.relacioncurso2.nota}.")

#Segunda Notal del curso 2 del Alumno en el curso
alumno1.relacioncurso2.nota = 15

print (f"El Alumno {alumno1.nombre} esta inscrito en el Curso {alumno1.relacioncurso2.nombre} posee una nota de {alumno1.relacioncurso2.nota}.")

#Tercera relación entre Alumno y Universidad
universidad1 = Universidad("UPANA")

alumno1.relacionuniversidad = universidad1

print(f"El Alumno {alumno1.nombre} esta inscrito en la Universidad {alumno1.relacionuniversidad.nombre}.")

