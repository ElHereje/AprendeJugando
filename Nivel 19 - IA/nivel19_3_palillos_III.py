"""

Se trata de que dos jugadores por turnos van quitando
palillos en unas cantidades determinadas (entre 1 y 3
cada turno). El que quite el último gana

Estructura:
            JUEGOS DE LOS PALILLOS (NIM)

1. presentación
2. Elección del nivel (usuario)
3. Elección aleatoria de palillos (16-23)
4. Elección aleatoria del número de quitas (entre 1 y 3/4/5)
5. El jugador humano comienza primero
6. mostrar área de juego con palillos
7. Turno de usuario humano
    Elige palillos a quitar
    Se muestra área de juego sin esos palillos
    Cambio de turno
8. Turno ordenador
    Si es nivel fácil, elige aleatoriamente
    Si es difícil, se llama a IA
    Se muestra área de juego sin esos palillos
    Cambio de turno
9. Después de cada movimiento se comprueba si no hay más palillos
    Si es así, se comprueba quién cogió el último
    Se muestra ganador
10. Si aún hay palillos, se sigue con el turno siguiente

Implementamos la IA:
    Si las quitas son hasta 5, habrá que dejar en la mesa múltiplos de 6:
        19%6=1 --> se quita 1
        15%6=3 --> se quita 3
    Si las quitas son hasta 4, habrá que dejar en la mesa múltiplos de 5:
        16%5=1 --> se quita 1
        18%5=3 --> se quita 3
    ....
por lo tanto  palillos_quitar = palillos % (quitas+1)


"""

# importamos los módulos necesarios
import random
import time
import os  # para limpiar la pantalla


def presentacion_1():
    """Mostramos pantalla de inicio y devuelve
        el nivel fácil o difícil que elije el usuario"""

    print()
    print("   ************  JUEGO DE LOS PALILLOS   ************")
    print()
    print()
    print("           gana quien coge el último palillo      ")
    print()
    print()
    print("            1- fácil     /     2- Difícil")
    print()
    print()
    print("   **************************************************")
    print()

    nivel = ""

    while nivel != "1" and nivel != "2":
        nivel = input("   Elige nivel (1/2): ")
    return nivel


def presentacion_2(palillos, quitas):
    """Mostramos una segunda pantalla con los datos del juego,
        y pedimos al usuario que de enter para empezar"""
    print()
    print("   ************  JUEGO DE LOS PALILLOS   ************")
    print()
    print()
    print(f"                   Habrá {palillos} en total      ")
    print()
    print(f"          Se pueden quitar entre 1 y {quitas} palillos")
    print()
    print("                 Empiezas a mover tú...")
    print()
    print("   **************************************************")
    print()
    input("    Pulsa enter para empezar.....")



def sorteo_opciones():
    """devuelve dos valores aleatorios: Nº de palillos
            (entre 16 y 23) y nº de palillos a quitar (entre 3 y 5)"""
    palillos = random.randint(16, 23)
    quitas = random.randint(3, 5)
    return palillos, quitas


def area_de_juego(palillos, quitas):
    """Muestra los palillos que hay en cada jugada de la partida"""

    print()
    print("   ************  JUEGO DE LOS PALILLOS  ************")
    print()
    print()

    for fila in range(4):
        print(end="  ")
        for p in range(1, palillos+1):
            print("|", end="  ") # una barra por cada palillo
            if p % quitas == 0:
                print(end=" ") # agrupamos los palillos por nº de quitas
        print()
    print()
    print()
    print()



def movimiento_jugador(palillos, quitas):
    """Devuelve el nº de palillos que el usuario quita en cada jugada"""

    if quitas == 3:
        quitas = ("1", "2", "3")
    elif quitas == 4:
        quitas = ("1", "2", "3", "4")
    elif quitas == 5:
        quitas = ("1", "2", "3", "4", "5")
    q = input("   palillos a quitar: ")
    while q not in quitas or int(q) > palillos:
        if q not in quitas:
            q = input(f"   Elige entre 1 y {len(quitas)}")
        elif int(q) > palillos:
            q = input(f"   Sólo quedan {palillos} palillos")
    else:
         palillos_quitar = int(q)

    return palillos_quitar


def movimiento_ordenador_aleatorio(palillos, quitas):
    """Devuelve nº aleatorio de palillos a quitar como jugada del ordenador"""

    palillos_quitar = random.randint(1, quitas)
    while palillos_quitar > palillos: # mientras el nº sea mayor al nº de palillos
                                      # seguirá pidiendo.
        palillos_quitar = random.randint(1, quitas)

    return palillos_quitar


def movimiento_ordenador_ia(palillos, quitas):
    """Devuelve nº aleatorio de palillos a quitar como jugada del ordenador
        calculados para que el ordenador gane siempre que pueda """

    # Si se pueden quitar 3, hay que dejar 4 o múltiplos de 4
    # Si se pueden quitar 4, hay que dejar 5 o múltiplos de 5
    # Se trata de dejar siempre un palillo más de los que se pueden quitar
    # ganará el que deje múltiplos de quitas más uno

    palillos_quitar = None

    while palillos_quitar is None or palillos_quitar > palillos:
        if palillos <= quitas: # si se pueden quitar todos...
            palillos_quitar = palillos
        elif palillos % (quitas+1) == 5:
            palillos_quitar = 5
        elif palillos % (quitas+1) == 4:
            palillos_quitar = 4
        elif palillos % (quitas+1) == 3:
            palillos_quitar = 3
        elif palillos % (quitas+1) == 2:
            palillos_quitar = 2
        elif palillos % (quitas+1) == 1:
            palillos_quitar = 1
        elif palillos % (quitas+1) == 0: # si no hay resto...
            palillos_quitar = random.randint(1, 2)

    return palillos_quitar


def mostrar_ganador(turno):
    """Muestra pantalla final con ganador de a partida"""

    if turno == 2:
        mensaje1 = "             HAS COGIDO EL ÚLTIMO PALILLO"
        mensaje2 = "              ****    HAS GANADO    ****"
    elif turno == 1:
        mensaje1 = "           EL ORDENADOR COGE EL ÚLTIMO PALILLO"
        mensaje2 = "              ****    HAS PERDIDO    ****"

    print()
    print("   ************  JUEGO DE LOS PALILLOS  ************")
    print()
    print()
    print()
    print(f"{mensaje1}")
    print()
    print()
    print(f"{mensaje2}")
    print()
    print()
    print()
# ---------------------- Programa Ppal --------------------------------------


# flujo del programa
turno = 1 # el jugador humano es el turno 1
palillos, quitas = sorteo_opciones()

os.system("cls") # limpiamos la pantalla
nivel = presentacion_1()

os.system("cls")
presentacion_2(palillos, quitas)

jugando = True

while jugando:
    os.system("cls")
    area_de_juego(palillos, quitas)

    if turno == 1:
        jugada = movimiento_jugador(palillos, quitas)
        turno = 2
    elif turno == 2:
        print("El ordenador está pensando....")
        time.sleep(2)
        if nivel == "1":
            jugada = movimiento_ordenador_aleatorio(palillos, quitas)
        elif nivel == "2":
            jugada = movimiento_ordenador_ia(palillos, quitas)
        turno = 1

    palillos -= jugada

    if palillos == 0:
        os.system("cls")
        mostrar_ganador(turno)
        jugando = False


# ----------------------------------------------------------------------------
