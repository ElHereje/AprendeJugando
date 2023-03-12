'''
En este cod. vamos a codificar las opciones para marcar o desmarcar las minas, 
es decir, si creemos que hay una mina, poner una vandera con la letra "b".
También usaremos el "Algoritmo de relleno por difusión", para el caso que 
al marcar una casilla sea cero --> desvelaremos los ceros adyacentes y las pistas
que los limitan --> rellanado()

'''

import random
import os

def crear_tablero(fil, col, val):
    
    '''Crea una matriz con las filas y columnas y valor que le pasamos'''
    
    tablero = []
    for i in range(fil):
        tablero.append([])
        for j in range(col):
            tablero[i].append(val)
    return tablero

def muestra_tablero(tablero):
    
    '''Muestra en filas y columnas la matriz que le pasemos'''
    
    print("* * * * * * * * * * * * * * * * * *")
    for fila in tablero:
        print("*", end=" ")
        for elem in fila:
            print(elem, end=" ")
        print("*")
    print("* * * * * * * * * * * * * * * * * *")
        
def coloca_minas(tablero, minas, fil, col):
    
    '''Coloca en el tablero que le pasamos el nº de minas que le pasemos'''
    
    minas_ocultas = [] # coordenadas
    numero = 0
    while numero < minas:
        y = random.randint(0, fil - 1)
        x = random.randint(0, col - 1)
        # tablero[y][x] = tablero[i][j]
        if tablero[y][x] != 9:
            tablero[y][x] = 9
            numero += 1
            minas_ocultas.append((y, x))
    return tablero, minas_ocultas



def coloca_pistas(tablero, fil, col):
    
    '''Recorre el tablero y pone el nº de minas vecinas que tiene cada casilla'''
    
    # recorremos todas las casillas:
    for y in range(fil):
        for x in range(col):
            # comprobamps si es una mina
            if tablero[y][x] == 9:
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if 0 <= y+i <= fil-1 and 0 <= x+j <= col-1: # para no salirnos..
                            if tablero[y+i][x+j] != 9:
                                tablero[y+i][x+j] += 1
    return tablero


# Algoritmo de relleno
def rellenado(oculto, visible, y, x, fil, col, val):
    
    '''recorre todas las casillas vecinas, y comprueba si son ceros, si es así las
    descubre y recorre las vecinas a esta, hasta encontrar casillas con pistas, que
    también las descubre'''
    
    ceros = [(x,y)] # lista donde guardamos los ceros que encontrams
    while len(ceros) > 0:
        y, x = ceros.pop() # sacamos esas corrdenadas de la lista
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= y+i <= fil-1 and 0 <= x+j <= col-1:
                    if visible[y+i][x+j] == val and oculto[y+i][x+j] == 0:
                        visible[y+i][x+j] = 0
                        if (y+i, x+j) not in ceros: # verificamos que ya están las coord.
                            ceros.append((y+i, x+j))
                    else:
                        # si no es cero, es una pista
                        visible[y+i][x+j] = oculto[y+i][x+j] 
    return visible
                 


def tablero_completo(tablero, fil, col, val):
    '''Comprueba si el tablero no tiene ninguna casilla con el valor visible inicial'''
    
    for y in range(fil):
        for x in range(col):
            if tablero[y][x] == val:
                return False
    return True



def presentacion():
    
    '''Pantalla de presentación'''
    
    os.system("cls")
    
    print("********************************")
    print("*                              *")
    print("*          BUSCAMINAS          *")
    print("*                              *")
    print("*       w/a/s/d - moverse      *")
    print("*                              *")
    print("*          m - mostrar         *")
    print("*                              *")
    print("*    b/v  - marcar/desmarcar   *")
    print("*                              *")
    print("*                              *")
    print("********************************")
    print()
    input(" 'Enter' para empezar...")
    
    
def menu():
    
   '''Devuelve el movimiento u opción elegida por el usuario'''
   
   print()
   opcion = input("w/a/s/d - m - b/v : ")
   return opcion
    
    
    
def reemplaza_ceros(tablero):
    for i in range(12):
        for j in range(16):
            if tablero[i][j] == 0:
                tablero[i][j] = " "
    return tablero
    

        
        
 ################  Flujo del programa ################
 
columnas = 16
filas = 12

visible = crear_tablero(filas, columnas, "-")
oculto = crear_tablero(filas, columnas, 0)  # valores iniciales 
# por defecto ponemos 15 minas, podríamos hacer que lo eligiera el jugador...
oculto, minas_ocultas = coloca_minas(oculto, 15, filas, columnas)

oculto = coloca_pistas(oculto, filas, columnas)

presentacion()

# Colocamos ficha inicial y mostramos tablero

y = random.randint(2, filas-3) # 3 porque cogemos una central
x = random.randint(2, columnas-3)

# antes de colocar la ficha, guardamos su valor en na variable temporal, para
# no perderlo, para poder recuperar ese valor después de moverse:
real = visible[y][x]
#...luego ya podemos poner la casilla
visible[y][x] = "x"

os.system("cls")

muestra_tablero(visible)

# Bucle ppal

minas_marcadas = []

jugando = True

while jugando:
    
    mov = menu()
    # definimos los movimientos (w, s, a ,d)
    if mov == "w": # arriba
        if y == 0:  # si estamos arriba del todo...
            y = 0
        else:
            visible[y][x] = real
            y -= 1
            real = visible[y][x]
            visible[y][x] = "x"
            
    elif mov == "s": # abajo
        if y == filas - 1: # si ya estamos abajo
            y = filas - 1
        else:
            visible[y][x] = real
            y += 1
            real = visible[y][x]
            visible[y][x] = "x"

    elif mov == "a":
        if x == 0: # si ya estamos en la izq
            x = 0
        else:
            visible[y][x] = real
            x -= 1
            real = visible[y][x]
            visible[y][x] = "x"
            
    elif mov == "d":
        if x == columnas - 1: # si ya estamos en la derecha
            x = columnas - 1
        else:
            visible[y][x] = real
            x += 1
            real = visible[y][x]
            visible[y][x] = "x"
            
    # definimos si ponemos una bandera (b)
    elif mov == "b":
        if real == "-": # verificamos que aún no se ha levantado
            visible[y][x] = "#"
            real = visible[y][x]
            if (x,y) not in minas_marcadas:
                minas_marcadas.append((x,y))
                
    # definimos si queremos desmarcar la casilla ("v")
    elif mov == "v":
        if real == "#": # verificamos que aún no se ha levantado
            visible[y][x] = "-"
            real = visible[y][x]
            if (x,y) in minas_marcadas:
                minas_marcadas.remove((x,y))
    
    # definimos lasopciones de "mostrar" ("m")
    elif mov == "m":
        if oculto[y][x] == 9: # levantamos una mina...
            visible[y][x] = "@"
            jugando = False
            
        elif oculto[y][x] != 0: # si es una pista...
            visible[y][x] = oculto[y][x]
            real = visible[y][x]
            
        elif oculto[y][x] == 0: 
            visible[y][x] = 0
            # desvelamos las casillas que sean cero que estén adyacente
            visible = rellenado(oculto, visible, y, x, filas, columnas, "-")
            visible = reemplaza_ceros(visible)
            real = visible[y][x]
    
    
    os.system("cls")
    muestra_tablero(visible)
    
    ganas = False
    
    if tablero_completo(visible, filas, columnas, "-") and \
        sorted(minas_ocultas) == sorted(minas_marcadas) and \
        real != "-":
            ganas = True
            jugando = False
            
if not ganas:
    print("-------------------------")
    print("------ Has Perdido ------")
    print("-------------------------")
else:
    print("-------------------------")
    print("------- Has ganado ------")
    print("-------------------------")
    
print()
input(" 'Enter' para salir ... ")