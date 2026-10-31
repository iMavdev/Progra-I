from libro import Libro
from biblioteca import Biblioteca

obj_libro1 = Libro("L001", "Cien Años de Soledad", "Gabriel García Márquez")
obj_libro2 = Libro("L002", "El Principito", "Antoine de Saint-Exupéry")
obj_libro3 = Libro("L003", "Don Quijote de la Mancha", "Miguel de Cervantes")
obj_libro4 = Libro("L004", "1984", "George Orwell")
obj_libro5 = Libro("L005", "La Odisea", "Homero")

obj_biblioteca = Biblioteca("Dr. Gutierrez")

print ("Agregando libros a la biblioteca:")
obj_biblioteca.agregar_libro(obj_libro1)
obj_biblioteca.agregar_libro(obj_libro2)
obj_biblioteca.agregar_libro(obj_libro3)
obj_biblioteca.agregar_libro(obj_libro4)
obj_biblioteca.agregar_libro(obj_libro5)

print("\nMostrando libros en la biblioteca:")
obj_biblioteca.mostrar_libros()

print ("\nBuscando libro en la biblioteca:")
libro_encontrado = obj_biblioteca.buscar_libro(obj_libro2.codigo)

if libro_encontrado:
    print(f"El libro con código {obj_libro2.codigo} está registrado en la biblioteca: {libro_encontrado.titulo}")
else:
    print(f"El libro con código {obj_libro2.codigo} no está registrado en la biblioteca.")


print ("\nIntentando agregar libro repetido")
obj_biblioteca.agregar_libro(obj_libro1)

print("\nEliminando libro de la biblioteca:")
obj_biblioteca.eliminar_libro(obj_libro1.codigo)

print("\nMostrando libros actualizados en la biblioteca:")
obj_biblioteca.mostrar_libros()