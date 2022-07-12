#Importaciones
import functions as fn
import platform
#Inicializaciones

#Entrada al programa
print("*"*5,"Bienvenido a Casilleros.com","*"*5)

#Menú
sw = 0
while sw == 0:
    option = (input("¿Qué desea realizar? Elija una opción:\n1. Arrendar un casillero.\n2. Ver casilleros disponibles.\n3. Asignar un nombre a un casillero.\n4. Mostrar casilleros con nombre.\n5. Anular casillero arrendado. \n6. Mostrar total a pagar. \n7. Mostrar total de ventas.\n8. Salir.\n"))
    #Opción 1: Arrendar casilleros
    if option == "1":
        print("Los casilleros disponibles son los siguientes:")
        fn.dispon()
        arr_casill=input("¿Qué casillero desea arrendar?")
        fn.arrendar(arr_casill)
        pass
    #Opción 2: Casilleros disponibles
    elif option == "2":
        fn.casill_actual()
    #Opción 3: Asignar nombre a casillero
    elif option == "3":
        pass
    #Opción 4: Mostrar casilleros con nombre
    elif option == "4":
        pass
    #Opción 5: Anular casillero
    elif option == "5":
        pass
    #Opción 6: Mostrar valor a pagar
    elif option == "6":
        pass
    #Opción 7: Mostrar total ventas
    elif option == "7":
        pass
    #Opción 8: Salir
    elif option == "7":
        print("Muchas gracias por su visita.\nSaliendo del programa...")
        sw=1
    #Error
    else:
        fn.clear()
        print("Ingresó una opción incorrecta. Intente nuevamente.")
        skip=input("Presione cualquier tecla para continuar.")
        fn.clear()
