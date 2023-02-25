'''
vamos a necesitar dos tableros:
- Uno visible, donde NO se vean lo que contienen las casillas
- Otro oculto, donde esté la información oculta de las casillas


En este cod, represenamos el tablero y definimos los movimientos.
También colocaremos las minas por el tablero (estarán ocultas)

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
    
    for fila in tablero:
        for elem in fila:
            print(elem, end=" ")
        print()
        
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
    
        
        
 ################  Flujo del programa ################
 
columnas = 16
filas = 12

visible = crear_tablero(filas, columnas, "-")
oculto = crear_tablero(filas, columnas, 0)  # valores iniciales 
# por defecto ponemos 15 minas, podríamos hacer que lo eligiera el jugador...
oculto, minas_ocultas = coloca_minas(oculto, 15, filas, columnas)

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
            
    os.system("cls")
    muestra_tablero(visible)