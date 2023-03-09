"""Implementamnos los movimientos, la función ganador"""


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



def mover_derecha(t):
    '''Mueve las casillas a la dcha y realiza las mezclas'''
    '''vamos a considerar la situación mas simple t[0,0,2,0]
    t[0,0,2,0]
    mezclas = []
    for i in range(len(t)-1):
        for x in range(-2, -len(t)-1, -1):
            if t[x] != 0 and t[x+1] == 0:
                t[x+1] = t[x]
                t[x] = 0
            elif t[x] != 0 and t[x+1] = t[x] and \
                x+1 not in mezclas and x not in mezclas:
                t[x+1] *= 2
                t[x] = 0
                mezclas.append[x+1]
    '''
    mov = 0
    for y in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for x in range(-2, -len(t)-1, -1):
                if t[y][x] != 0 and t[y][x+1] == 0:
                    t[y][x+1] = t[y][x]
                    t[y][x] = 0
                    mov += 1
                elif t[y][x] != 0 and t[y][x] == t[y][x+1] and \
                    x not in mezclas and x-1 not in mezclas:
                    t[y][x+1] *= 2
                    t[y][x] = 0
                    mezclas.append(x)
                    mov += 1
    return t,mov


def mover_arriba(t):
    mov = 0
    for x in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for y in range(1, len(t)):
                if t[y][x] != 0 and t[y-1][x] == 0:
                    t[y-1][x] = t[y][x]
                    t[y][x] = 0
                    mov += 1
                elif t[y][x] != 0 and t[y][x] == t[y-1][x] and \
                    x not in mezclas and x-1 not in mezclas:
                    t[y-1][x] *= 2
                    t[y][x] = 0
                    mezclas.append(y)
                    mov += 1
    return t,mov

def mover_abajo(t):
    mov = 0
    for x in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for y in range(-2, -len(t)-1, -1):
                if t[y][x] != 0 and t[y+1][x] == 0:
                    t[y+1][x] = t[y][x]
                    t[y][x] = 0
                    mov += 1
                elif t[y][x] != 0 and t[y][x] == t[y+1][x] and \
                    x not in mezclas and x-1 not in mezclas:
                    t[y+1][x] *= 2
                    t[y][x] = 0
                    mezclas.append(y)
                    mov += 1
    return t,mov

def mover_izquierda(t):
    mov = 0
    for y in range(len(t)):
        mezclas = []
        for i in range(len(t)-1):
            for x in range(1, len(t)):
                if t[y][x] != 0 and t[y][x-1] == 0:
                    t[y][x-1] = t[y][x]
                    t[y][x] = 0
                    mov += 1
                elif t[y][x] != 0 and t[y][x] == t[y][x-1] and \
                    x not in mezclas and x-1 not in mezclas:
                    t[y][x-1] *= 2
                    t[y][x] = 0
                    mezclas.append(x)
                    mov += 1
    return t,mov


def ganador(tablero):
    '''Devuelve True si se alcanza la cifra indicada'''

    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 2048:
                return True
    return False


def sin_movimiento(tablero):
    ''' Recorre el tablero y comprueba si hay más movimientos'''

    final = True
    for y in range(len(tablero)):
        for x in range(len(tablero)-1):
            if tablero[y][x] == tablero[y][x+1]:
                final = False
    for x in range(len(tablero)-1):
        for x in range(len(tablero)):
            if tablero[y][x] == tablero[y+1][x]:
                final = False
    return final


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

    else:
        if jugada == "d":
            tablero, movimientos = mover_derecha(tablero)

        elif jugada == "a":
            tablero, movimientos = mover_izquierda(tablero)

        elif jugada == "w":
            tablero, movimientos = mover_arriba(tablero)

        elif jugada == "s":
            tablero, movimientos = mover_abajo(tablero)


    if ganador(tablero) and not mostrar_ganado:
        mostrar_ganado = True
        os.system("cls")
        mostrar_tablero(tablero)
        print("-------- HAS GANADO --------")
        op = input("¿Quieres continuar? (s/n): ")
        if op != "s":
            break

    if len(casillas_vacias(tablero)) == 0 and sin_movimiento(tablero) == True:
        print("-------- HAS PERDIDO --------")
        print("-----------------------------")
        break


