#Importaciones
import functions as fn
import platform
#Inicializaciones

#Entrada al programa
print("*"*5,"Bienvenido a Casilleros.com","*"*5)

#Menú
sw = 0
while sw == 0:
    option=(input("¿Qué desea realizar? Elija una opción:\n1. Arrendar un casillero.\n2. Ver casilleros disponibles.\n3. Asignar un nombre a un casillero.\n4. Mostrar casilleros con nombre.\n5. Mostrar total a pagar.\n6. Mostrar total de ventas.\n7. Salir.\n"))
    #Opción 1
    if option == "1":
        pass
    #Opción 2
    elif option == "2":
        pass
    #Opción 3
    elif option == "3":
        pass
    #Opción 4
    elif option == "4":
        pass
    #Opción 5
    elif option == "5":
        pass
    #Opción 6
    elif option == "6":
        pass
    #Opción 7
    elif option == "7":
        print("Muchas gracias por su visita.\nSaliendo del programa...")
        sw=1
    #Error
    else:
        fn.clear()
        print("Ingresó una opción incorrecta. Intente nuevamente.")
        skip=input("Presione cualquier tecla para continuar.")
        fn.clear()
