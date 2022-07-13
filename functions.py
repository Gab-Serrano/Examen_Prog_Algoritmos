#Importaciones
from time import sleep
import numpy as np
import os
import platform

#Inicializaciones
list_casilleros=['101','102','103','104','105','106','107','108','109']

#Matrices
#Mapa de casilleros
mapa_casilleros = np.empty((3,3), dtype=('U',15))
cont=101
for i in range(3):
    for j in range(3):
        mapa_casilleros[i,j]=cont
        cont+=1
casilleros = mapa_casilleros.copy()
casill_nombre = mapa_casilleros.copy()

#Casilleros disponibles para arrendar
def dispon ():
    for i in range(3):
        for j in range(3):
            if casilleros[i, j] in list_casilleros:
                print(mapa_casilleros[i, j])
            else:
                pass

#Casilleros actuales
def casill_actual():
    for i in casilleros:
        for j in i:
            sw=0
            while sw == 0:
                print("|",j,end="| ")
                sw+=1
        print("")

#Limpiar pantalla
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

#Función sumar monto de venta

def ventas(asiento, total_compra=0):
    if asiento in ['101', '102', '103']:
        total_compra += 10000
    elif asiento in ['104', '105', '106']:
        total_compra += 5000
    else:
        total_compra += 3000
    return total_compra
                
# Función arrendar casilleros

def arrendar(num_casillero):
    for i in range (3):
        for j in range(3):
            if casilleros[i, j] == num_casillero:
                casilleros[i, j] = " X "
            else:
                pass

#Función nombrar casillero
def reemplazar_nombre (casillero,nombre):
    for i in range(3):
        for j in range(3):
            if mapa_casilleros[i,j] == casillero:
                index = np.where(mapa_casilleros == casillero)
                casill_nombre[tuple(index)] = nombre
            else:
                continue

#Casilleros actuales con nombre
def casill_nom_actual():
    for i in casill_nombre:
        for j in i:
            sw = 0
            while sw == 0:
                if j in list_casilleros:
                    print("|   ------   ",end="|")
                elif len(j) < 10:
                    espacio = 10-len(j)
                    print("|", " "*espacio, j, end="|")
                sw += 1
        print("")

#Función anular venta

def anular(casillero):
    for i in range(3):
        for j in range(3):
            if mapa_casilleros[i, j] == casillero:
                index = np.where(mapa_casilleros == casillero)
    casilleros[tuple(index)] = mapa_casilleros[tuple(index)]
    casill_nombre[tuple(index)] = mapa_casilleros[tuple(index)]


#-------------------------------------------------------------------------------------------------------------------------------------------
#Funciones 2
#Borrado consola

def clear():
    os.system('cls')
    os.system('clear')


#clear()

#Continuar - borrado de consola

def ir_menu():
  sleep(1)
  next = input("\nPara volver al menú principal presione una tecla.")
  clear()

#Mostrar asientos disponibles
#Según el requisito: Mostrará por pantalla todos los asientos disponibles con su número de asiento y los no disponibles los con una “X”


def disp_asiento(mapa_avion):  # agrego nombre más claro.
  print("*"*3, "Asientos del  avión", "*"*3)
  print()
  for i in range(9):
    for j in range(9):
      print(mapa_avion[i][j], end=" ")
    print()
  print()
  print("1.Asientos normales: del 1 al 30. \n2.Asientos VIP: del 31 al 42.")
  print()

#Contar asientos ocupados


def cant_ocupado(mapa_avion):
  cant_ocupados = 0
  for fila in mapa_avion:  # indexación de cada fila de la matriz
    for asiento in fila:  # indexación en cada valor de cada fila
      if asiento == "X" or asiento == " X":  # si algun valor es X, retorna disponibildiad
        cant_ocupados += 1
  print("Asientos ocupados:", cant_ocupados)
  print()
  return cant_ocupados


#Funcion telefono
validacion = True

def validar_telefono():
  cont = 0
  while validacion:
    try:
      telefono = int(
          input("\nIngrese su numero de telefono: (comenzar con el numero 9)\t"))
      if len(str(telefono)) == 9:
        for i in str(telefono):
          if "9" in i:
            break
          else:
            cont += 1
        if cont >= 1:
          print("\nError, Su Telefono debe tener un 9 al principio")
          cont = 0
        else:
          break
      else:
        print("\nError, su numero debe tener 9 digitos")
    except ValueError:
      print("\nError, ingrese su telefono como numeros")
  return telefono

#Funcion compra

def compra(compra_asiento, banco, avion, asiento, normal, vip, total):
  disp_avion = avion.strip()
  donde = np.where(disp_avion == asiento)
  avion[tuple(donde)] = " X"
  if compra_asiento > 0 and compra_asiento <= 30:
    normal += 78900
    print("\n")
    print("*"*40)
    print("Boleta:")
    print("* ", "asientos normales:\t$", round(normal))
    if banco:
      descuento = normal * 0.15
      normal = normal - descuento
      print("* ", "descuento 15%:\t$", round(descuento))
    print()
    print("*"*40)
  elif compra_asiento >= 31 and compra_asiento <= 42:
    vip += 240000
    print("\n")
    print("*"*40)
    print("Boleta:")
    print("* ", "asientos Vip:\t$", round(vip))
    if banco:
      descuento = vip * 0.15
      vip = vip - descuento
      print("* ", "descuento 15%:\t$", round(descuento))
    print()
    print("*"*40)
  total = total + vip + normal
  print("            su total es:\t$", round(total))
#Funcion modificar


def modificar_datos(opcion):
  if opcion == 1:
    print("\nModificando nombre: ")
    nom = str(input("\nIngrese su nuevo nombre: \t"))
    return nom
  elif opcion == 2:
    print("\nModificando telefono: ")
    telefono = validar_telefono()
    return telefono

def anular_pasaje(avion):
  mapa_avion = np.char.array([["|", " 1", " 2", " 3", "     ", " 4", " 5", " 6", "|"], ["|", " 7", " 8", " 9", "     ", "10", "11", "12", "|"],
                              ["|", "13", "14", "15", "     ", "16", "17", "18", "|"], [
                                  "|", "19", "20", "21", "     ", "22", "23", "24", "|"],
                              ["|", "25", "26", "27", "     ", "28", "29", "30", "|"], [
                                  "|―", "――", "――", "―", "     ", "―", "――", "――", "―|"],
                              ["|_", "__", "__", "_", "     ", "_", "__", "__", "_|"], [
                                  "|", "31", "32", "33", "    ", "34", "35", "36", "|"],
                              ["|", "37", "38", "39", "     ", "40", "41", "42", "|"]])
  while validacion:
    try:
      asiento_nul = int(
          input("\nIngrese el asiento que desea anular o ingrese 0 para salir: "))
      asiento2 = str(asiento_nul)
      check_avion = valid_compra(asiento2, avion)
      if asiento_nul > 0 and asiento_nul <= 42 and check_avion == False:
        asiento_nul = str(asiento_nul)
        print("\nEl asiento:", asiento_nul, "fue eliminado...")
        break
      elif asiento_nul == 0:
        print("\nVolviendo al menu..")
        break
      elif check_avion == True:
        print("\nError: El asiento esta libre actualmente")
      else:
        print("\nError: Ingrese un numero entre el 1 y el 42")
    except ValueError:
      print("\nError: Ingrese el asiento como un numero")
  if asiento_nul != 0:
    disp_mapa_avion = mapa_avion.strip()
    ub_anul_asiento = np.where(disp_mapa_avion == asiento_nul)
    if asiento_nul in ("1,2,3,4,5,6,7,8,9"):
      avion[tuple(ub_anul_asiento)] = " "+asiento_nul
    else:
      avion[tuple(ub_anul_asiento)] = asiento_nul
    return asiento_nul


def eliminar_datos(nombre, rut, telefono, banco):
  nombre = None
  rut = None
  telefono = None
  banco = None
  return nombre, rut, telefono, banco

#Función no comprar el mismo pasaje


def valid_compra(asiento, avion):
  raw_avion = avion.strip()
  if asiento in raw_avion:
    return True
  else:
    return False


#-------------------------------------------------------------------------------------------------------------------------------------
#Main matriz
casilleros = np.array([["", "", ""],
                       ["", "", ""],
                       ["", "", ""]], dtype=object)

clientes=[]

#Funciones casilleros 2

def arrendar(total_dia):
    print("*  Arrendar Casilleros  *")
    print(" ----------------------- ")
    print("   1. Nivel 1: $10.000   ")
    print("   2. Nivel 2: $5.000    ")
    print("   3. Nivel 3: $2.000    ")
    print(" ----------------------- ")

    opcion= int(input("Ingrese el nivel que desea:\n"))
    fila=opcion-1
    mostrar_fila(fila)
    opcion = int(input("Ingrese el número de casillero que desea:\n"))
    if fila == 0:
        colum= opcion-101
        total_dia+=10000
    elif fila == 1:
        colum = opcion-104
        total_dia += 5000
    else:
        colum = opcion-107
        total_dia += 3000
    nombre= input("Ingrese un nombre para reservar. (Solo se mostrarán 4 carácteres máximo).")
    clientes.append([nombre, opcion])
    print(clientes)
    casilleros[fila, colum] = nombre
    return total_dia

def mostrar():
    c = 100
    for i in casilleros:
        for j in i:
            sw = 0
            c+=1
            while sw == 0:
                if j == "":
                    print("|   ",c,end="   |")
                elif len(j) <= 3:
                    espace = 3-len(j)
                    print("|  "," "*espace,j, end="   |")
                elif len(j) > 3:
                    endLoc=j[:4]
                    print("|  ",endLoc, end="   |")
                sw += 1    
        print("")


def mostrar_fila(fila):
    if fila == 0:
        c = 100
    elif fila == 1:
        c = 103
    else:
        c = 106

    for i in casilleros[fila]:
        sw = 0
        c+=1
        while sw == 0:
            if i == "":
                print("|   ", c, end="   |")
            elif len(i) <= 3:
                espace = 3-len(j)
                print("|  ", " "*espace, j, end="   |")
            elif len(i) > 3:
                endLoc = i[:4]
                print("|  ", endLoc, end="   |")
            sw += 1
    print("")


def mostrar_ocupados():
    c = 100
    for i in casilleros:
        for j in i:
            sw = 0
            c += 1
            while sw == 0:
                if j == "":
                    print("|   ", c, end="   |")
                else:
                    print("|     X", end="    |")
                sw += 1
        print("")

def lista_reservas():
    for i in clientes:
        for j in i:
            print(j, end=" ")
        print("")
    if clientes == None:
        print("No hay clientes guardados.")

# Programa que define y llena una matriz con nombre del estudiante y 5 notas

columnas = 5
estudiantes = int(input("ingrese cantidad de estudiantes: "))
matriz = np.empty(shape=(estudiantes, columnas), dtype=('U', 15))

for i in range(estudiantes):
  nombre = input("ingrese nombre del estudiante")
  matriz[i, 0] = nombre
  for k in range(1, 5):
    nota = int(input(f"Ingrese nota {k}: "))
    matriz[i, k] = nota
print(matriz)
