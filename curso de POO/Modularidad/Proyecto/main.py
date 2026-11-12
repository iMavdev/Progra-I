from libro import Libro
from biblioteca import Biblioteca
from usuario import Usuario
from funciones import mostrar_menu

print("Inicializando biblioteca...")
obj_biblioteca = Biblioteca()

print("Aquí se registrará un libro")
obj_libro1 = Libro("L001", "Cien Años de Soledad", "Gabriel García Márquez", 1967, "disponible")
obj_libro2 = Libro("L002", "El Principito", "Antoine de Saint-Exupéry", 1943, "disponible")
obj_libro3 = Libro("L003", "Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "disponible")

print ("Agregando libros a la biblioteca...")
obj_biblioteca.agregar_libro(obj_libro1)
obj_biblioteca.agregar_libro(obj_libro2)
obj_biblioteca.agregar_libro(obj_libro3)

print("Aquí se registrará un usuario")
obj_usuario1 = Usuario("U001", "Juan Pérez", "juan.perez@hotmail.com")
obj_usuario2 = Usuario("U002", "María López", "maria.lopez@gmail.com")


obj_biblioteca.agregar_usuario(obj_usuario1)
obj_biblioteca.agregar_usuario(obj_usuario2)

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        print("-------------------------")
        codigo_libro = input("Ingrese el código del libro: ")
        if obj_biblioteca.buscar_libro(codigo_libro):
            print(f"Ya existe un libro con el código {codigo_libro}.")
        else:
            titulo_libro = input("Ingrese el título del libro: ")
            autor_libro = input("Ingrese el autor del libro: ")
            yearpublication_libro = int(input("Ingrese el año de publicación: "))

            obj_libro = Libro(codigo_libro,titulo_libro,autor_libro,yearpublication_libro,"disponible")

            obj_biblioteca.agregar_libro(obj_libro)

    elif opcion == "2":
        print("-------------------------")
        carnet_usuario = input("Ingrese el carnet del usuario: ")
        if obj_biblioteca.buscar_usuario(carnet_usuario):
            print(f"Ya existe un usuario con el carnet {carnet_usuario}.")
        else:
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            correo_usuario = input("Ingrese el correo del usuario: ")

            obj_usuario = Usuario(carnet_usuario, nombre_usuario, correo_usuario)

            obj_biblioteca.agregar_usuario(obj_usuario)

    elif opcion == "3":
        print("-------------------------")
        obj_biblioteca.mostrar_libros()
    elif opcion == "4":
        print("-------------------------")
        obj_biblioteca.mostrar_usuarios()
    elif opcion == "5":
        carnet = input("Ingrese el carnet del usuario: ")
        codigo = input("Ingrese el código del libro: ")

        usuario = obj_biblioteca.buscar_usuario(carnet)
        libro = obj_biblioteca.buscar_libro(codigo)

        obj_biblioteca.realizar_prestamo(usuario, libro)

    elif opcion == "6":
        print ("-------------------------")
        carnet = input("Ingrese el carnet del usuario: ")
        codigo = input("Ingrese el código del libro: ")
        

        usuario = obj_biblioteca.buscar_usuario(carnet)
        libro = obj_biblioteca.buscar_libro(codigo)

        obj_biblioteca.devolver_libro(usuario, libro)

    elif opcion == "7":
        print ("-------------------------")
        obj_biblioteca.mostrar_prestamos()

    elif opcion == "8":
        print ("-------------------------")
        buscar_libro = input("Ingrese el código del libro a buscar: ")
        obj_biblioteca.buscar_libro(buscar_libro, mostrar=True)

    elif opcion == "9":
        print ("-------------------------")
        buscar_usuario = input("Ingrese el carnet del usuario a buscar: ")
        obj_biblioteca.buscar_usuario(buscar_usuario, mostrar=True)
        
    elif opcion == "10":
        print("Saliendo del sistema... Gracias por usar el Sistema de Gestión de Biblioteca.")
        break
    else:
        print("Opción no válida.")