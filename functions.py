#Importaciones
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
