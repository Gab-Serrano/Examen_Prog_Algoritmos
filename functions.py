#Importaciones
import numpy as np
import os
import platform

#Inicializaciones

#Matrices
#Mapa de casilleros
mapa_casilleros = np.empty((3,3), dtype=('U',15))
cont=101
for i in range(3):
    for j in range(3):
        mapa_casilleros[i,j]=cont
        cont+=1
casilleros = mapa_casilleros.copy()
#Casilleros disponibles para arrendar
def dispon ():
    for i in range(3):
        for j in range(3):
            if mapa_casilleros[i, j] in "101,102,103,104,105,106,107,108,109":
                print(mapa_casilleros[i, j])
            else:
                pass

#Casilleros actuales
def casill_actual ():
    print(casilleros)
#Limpiar pantalla
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

#Imprimir casilleros actuales


# Función arrendar casilleros
def arrendar(num_casillero):
    for i in range (3):
        for j in range(3):
            if casilleros[i, j] == num_casillero:
                casilleros[i, j] = "Ocupado"
