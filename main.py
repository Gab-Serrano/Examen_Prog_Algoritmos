#Importaciones
import numpy as np
import functions as fn

total_ventas = 0
#Menú
opcion = 0
listadoDeOpciones = ["1","2","3","4","5"]
while opcion != "5":
    print("*******************************")
    print("*   ARRIENDO DE CASILLEROS    *")
    print("*-----------------------------*")
    print("*   1. Arrendar casilleros    *")
    print("*   2. Mostrar disponibles    *")
    print("*   3. Listar nombre clientes *")
    print("*   4. Calcular ganancias     *")
    print("*   5. Salir                  *")
    print("*******************************")
    opcion = input("Seleccione opcion:\n")

#Validación menú
    if opcion not in listadoDeOpciones:
        print("Opción erronea.")
        input("Presione Enter para continuar...")
        continue
    
#Ejecusión del menú
    # Arriendo
    if opcion == "1":
        total_ventas=fn.arrendar(total_ventas)
        print(total_ventas)

    # Mostrar
    elif opcion == "2":
        #fn.mostrar()
        fn.mostrar_ocupados()
    # Listar
    elif opcion == "3":
        print("*** Lista de clientes ***")
        fn.lista_reservas()
    # Calcular
    elif opcion == "4":
        print("Opcición 4")
        print(total_ventas)
    # Salir
    else:
        print("Saliendo del programa...")
