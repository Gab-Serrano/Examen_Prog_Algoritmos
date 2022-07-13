#Importaciones
import functions as fn
import platform
#Inicializaciones
total_venta = 0

#Entrada al programa
print("*"*5,"Bienvenido a Casilleros.com","*"*5)

#Menú
sw = 0
while sw == 0:
    option = input("¿Qué desea realizar? Elija una opción:\n1. Arrendar un casillero.\n2. Ver casilleros disponibles.\n3. Asignar un nombre a un casillero.\n4. Mostrar casilleros con nombre.\n5. Anular casillero arrendado. \n6. Mostrar total a pagar. \n7. Mostrar total de ventas.\n8. Salir.\n")
    #Opción 1: Arrendar casilleros
    if option == "1":
        fn.clear()
        print("Los casilleros disponibles son los siguientes:")
        fn.casill_actual()
        arr_casill=input("¿Qué casillero desea arrendar?\n")
        fn.arrendar(arr_casill)
        total_venta += fn.ventas(arr_casill)
        fn.clear()

    #Opción 2: Casilleros disponibles
    elif option == "2":
        fn.clear()
        print("Los asientos disponibles son los siguientes.")
        fn.casill_actual()
        skip=input("Presione cualquier tecla para continuar.")
        fn.clear()

    #Opción 3: Asignar nombre a casillero
    elif option == "3":
        fn.clear()
        casill=input("Ingrese el número de casillero arrendado:\n")
        nom_casill=input("¿Qué nombre desea asignarle?\n")
        fn.reemplazar_nombre(casill,nom_casill)
        fn.clear()
    #Opción 4: Mostrar casilleros con nombre
    elif option == "4":
        fn.clear()
        print("Estos son los casilleros con nombre:\n")
        fn.casill_nom_actual()
        skip = input("Presione cualquier tecla para continuar.")
        fn.clear()
    #Opción 5: Anular casillero
    elif option == "5":
        fn.clear()
        casill = input("Ingrese el número de casillero que desea anular:\n")
        fn.anular(casill)
        fn.clear()
    #Opción 6: Mostrar valor a pagar
    elif option == "6":
        fn.clear()
        print("Monto total a pagar por el arriendo:\n")
        print("$",total_venta)
        skip = input("Presione cualquier tecla para continuar.")
    #Opción 7: Salir
    elif option == "7":
        print("Muchas gracias por su visita.\nSaliendo del programa...")
        sw=1
    #Error
    else:
        fn.clear()
        print("Ingresó una opción incorrecta. Intente nuevamente.")
        skip=input("Presione cualquier tecla para continuar.")
        fn.clear()
