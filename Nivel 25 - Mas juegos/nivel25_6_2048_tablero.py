"""En esta primara parte, creamos el tablero y lo rellenamos con los valores iniciales"""


# importamos los módulos ecesarios
import random
import os
import copy # necesario para hacer una copia del tablero


# creamos una matriz cuadrada cero con las dimensiones que le pasemos
# que sea cuadrada significa que tiene filas = columnas
def crea_tablero(fil):
    '''Crea una matriz con las filas y columnas, y el valor que le pasemos'''

    tablero = []
    for i in range(fil):
        tablero.append([])
        for j in range(fil):
            tablero[i].append(0)
    return tablero


#
def mostrar_tablero(tablero):
    '''Crea copia del tablero con espacios vacíos en vez de ceros y muestra la copia'''

    # hacemos una copia del tablero sustituyendo ceros por espacios vacios:
    t = copy.deepcopy(tablero)
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i][j] == 0:
                t[i][j] = " "

    # pintamos las rallitas vert. y horiz. del tablero
    print("-" * ((7 * len(t) + 1)))
    for i in range(len(t)):
        for j in range(len(t)):
            print("| {:4}".format(t[i][j]), end=" ")
        print("|")
        print("-" * ((7 * len(t) +1)))


def casillas_vacias(tablero):
    '''Devuelve una lista con las casillas vacías del tablero, necesario para
    poder introducir en ellas un nuevo nº'''

    vacias = []
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == 0:
                vacias.append([i, j])
    return(vacias)


def rellenar_casillas(tablero, vacias):
    '''Devuelve tablero con casilla aleatoria rellena con 90% de 2 ó 10% de 4'''

    n = random.choice([2,2,2,2,2,2,2,2,2,4])
    casilla = random.choice(vacias)
    tablero[casilla[0]][casilla[1]] = n
    return(tablero)



########## FLUJO DEL PROGRAMA ###########

tablero = crea_tablero(4) # tablero de 4x4
vacias = casillas_vacias(tablero)
tablero = rellenar_casillas(tablero, vacias)
movimientos = 1 # si hay movimierntos, rellenamos la casilla
mostrar_ganado = False

while True:
    os.system("cls")

    if movimientos != 0: # ha ha habido movimientos
        vacias = casillas_vacias(tablero)
        tablero = rellenar_casillas(tablero, vacias)
    
    jugada = ""
    while jugada not in ("a", "s", "w", "d"):
        os.system("cls")
        mostrar_tablero(tablero)
        jugada = input("    Mueve (w/a/s/d) --> ")


