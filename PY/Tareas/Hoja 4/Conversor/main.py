import longitud
import temperatura

# Variable para el menú principal
menu_principal = 0 #=0 porque el menú principal se ejecutará mientras la variable sea diferente de 3, que es la opción de salir del programa.

while menu_principal != 3:
    print("\n--- MENÚ CONVERSOR DE UNIDADES ---")
    print("1. Conversión de Longitud")
    print("2. Conversión de Temperatura")
    print("3. Salir")
    
    menu_principal = int(input("Elige una opción: "))
    
    if menu_principal == 1:
        # Variable para el submenú_longitud
        submenu_longitud = 0 #=0 porque el submenú de longitud se ejecutará mientras la variable sea diferente de 5, que es la opción de volver al menú principal.
        
        while submenu_longitud != 5:
            print("\n--- CONVERSIÓN DE LONGITUD ---")
            print("1. Metros a kilómetros")
            print("2. Kilómetros a metros")
            print("3. Metros a pies")
            print("4. Pies a metros")
            print("5. Volver al menú principal")
            
            submenu_longitud = int(input("Elige una opción: "))
            
            if submenu_longitud == 1:
                print("Has elegido Metros a kilómetros.")
                metros = 1000
                kilometros = metros_a_kilometros(metros)
                print(f"{metros} m = {kilometros} km")
            elif submenu_longitud == 2:
                print("Has elegido Kilómetros a metros")
                kilometros = 1
                metros = kilometros_a_metros(kilometros)
                print(f"{kilometros} km = {metros} m")
            elif submenu_longitud == 3:
                print("Has elegido Metros a pies")
                metros = 1
                pies = metros_a_pies(metros)
                print(f"{metros} m = {pies} ft")
            elif submenu_longitud == 4:
                print("Has elegido Pies a metros")
                pies = 3.28084
                metros = pies_a_metros(pies)
                print(f"{pies} ft = {metros} m")
            elif submenu_longitud == 5:
                print("Volviendo al menú principal...")
            else:
                print("Opción no válida.")
                
    elif menu_principal == 2:
        #variable para el submenú_temperatura
        submenu_temperatura = 0#=0 porque el submenú de temperatura se ejecutará mientras la variable sea diferente de 5, que es la opción de volver al menú principal.

        while submenu_temperatura != 5:
                    print("\n--- CONVERSIÓN DE TEMPERATURA ---")
                    print("1. Celsius a Fahrenheit")
                    print("2. Fahrenheit a Celsius")
                    print("3. Celsius a Kelvin")
                    print("4. Kelvin a Celsius")
                    print("5. Volver al menú principal")
                    
                    submenu_temperatura = int(input("Elige una opción: "))
                    
                    if submenu_temperatura == 1:
                        print("Has elegido Celsius a Fahrenheit.")
                        celsius = 25
                        fahrenheit = celsius_a_fahrenheit(celsius)
                        print(f"{celsius} °C = {fahrenheit} °F")
                    elif submenu_temperatura == 2:
                        print("Has elegido Fahrenheit a Celsius")
                        fahrenheit = 77
                        celsius = fahrenheit_a_celsius(fahrenheit)
                        print(f"{fahrenheit} °F = {celsius} °C")
                    elif submenu_temperatura == 3:
                        print("Has elegido Celsius a Kelvin")
                        celsius = 100
                        kelvin = celsius_a_kelvin(celsius)
                        print(f"{celsius} °C = {kelvin} K")
                    elif submenu_temperatura == 4:
                        print("Has elegido Kelvin a Celsius")
                        kelvin = 373.15
                        celsius = kelvin_a_celsius(kelvin)
                        print(f"{kelvin} K = {celsius} °C")
                    elif submenu_temperatura == 5:
                        print("Volviendo al menú principal...")
                    else:
                        print("Opción no válida.")
    elif menu_principal == 3:
        print("Saliendo del programa...")
    else:
        print("Opción no válida en el menú principal.")