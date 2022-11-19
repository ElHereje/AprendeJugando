"""
Tres en raya con IA

Tendrá 2 niveles

Cumplimentamos la IA difícil y optimizamos la fácil
"""

import random, time, os


def presentacion1():
    """Devuelve el nivel en el que se quiere jugar"""
    print()
    print("               TRES EN RAYA")
    print()
    print()
    print("                 1. Fácil")
    print("                 2. Difícil")
    print()
    print()
    print()

    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input("              --> ")
    return int(nivel)


def presentacion2():
    """Devuelve la ficha elegida por el humano y ordenador"""
    print()
    print("               TRES EN RAYA")
    print()
    print()
    print("                 Sale la ficha O")
    print("                  Elige: O / X")
    print()
    print()

    ficha = ""
    while ficha != "O" and ficha != "X":
        ficha = input("               --> ").upper()

    if ficha == "O":
        humano = "O"
        ordenador = "X"
    else:
        humano = "X"
        ordenador = "O"

    return humano, ordenador


def mostrar_tablero(tablero):
    """Muestra el tablero con las casillas vacías y puestas"""
    print()
    print("               TRES EN RAYA")
    print()
    print("        1       |2       |3")
    print(f"           {tablero[0]}    |    {tablero[1]}   |    {tablero[2]}")
    print("                |        |")
    print("        --------+--------+--------")
    print("        4       |5       |6")
    print(f"           {tablero[3]}    |    {tablero[4]}   |    {tablero[5]}")
    print("                |        |")
    print("        --------+--------+--------")
    print("        7       |8       |9")
    print(f"           {tablero[6]}    |    {tablero[7]}   |    {tablero[8]}")
    print("                |        |")
    print()


def seguir_jugando():  # true o false
    """True si quieres seguir, false si no"""
    print()
    respuesta = input("         Otra partida..(s/n) ?? : ").lower()
    if respuesta == "s" or respuesta == "si":
        return True
    else:
        return False


def hay_ganador(tablero, jugador):
    """Comprueba si un estado del tablero es ganador"""
    '''(comprueba si hay 3 fichas en línea'''
    if tablero[0] == tablero[1] == tablero[2] == jugador or \
            tablero[3] == tablero[4] == tablero[5] == jugador or \
            tablero[6] == tablero[7] == tablero[8] == jugador or \
            tablero[0] == tablero[3] == tablero[6] == jugador or \
            tablero[1] == tablero[4] == tablero[7] == jugador or \
            tablero[2] == tablero[5] == tablero[8] == jugador or \
            tablero[0] == tablero[4] == tablero[8] == jugador or \
            tablero[2] == tablero[4] == tablero[6] == jugador:
        return True
    else:
        return False


def tablero_lleno(tablero):  # true o false
    """Devuelve si está lleno o vacío"""
    """Si está lleno, significa empate"""
    for i in tablero:
        if i == " ":
            return False
    else:
        return True


def casilla_libre(tablero, casilla):
    """True si una casilla dada esta vacía y false si no"""
    return tablero[casilla] == " "


def movimiento_jugador(tablero):
    """Devuelve la casilla elegida por el jugador humano"""
    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("             Te toca (1-9): ")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion - 1):
                print("        Esa posición está ocupada.")
            else:
                return posicion - 1


def movimiento_ordenador_facil(tablero, jugador):
    """ va a revisiar solo las fichas del jugador humano, ya que"""
    """ el ordenador solo se defiende de ser ganado en la siguiente jugada"""
    """ VAmos recorriendo todas las posibles combinaciones de 2 fichas en """
    """ cuales, una tercera pondría fin al juego"""

    pass


def movimiento_ordenador_dificil(tablero, maquina, usuario):
    """Primero trata de ganar, luego evita ser ganado. Sino, si mueve 2º
        el ordenador intenta coger la casilla del medio, sino una esuqina.
        Si sale primero el ordenador, el 1er movimiento es aleatorio, pero
        en el 2º trata de coger la casilla del medio si está libre"""
    pass


# **********************  PROGRAMA PPAL  ************************

# variable que controla el bucle
jugando = True

# bucle ppal del juego
while jugando:
    # definimos el tablero
    tablero = [" "] * 9  # lista con 9 espacios vacíos
    os.system("cls")
    # ------------------------------------------------------
    # elegir nivel y ficha(turno)
    nivel = presentacion1()
    os.system("cls")

    humano, ordenador = presentacion2()  # fichas del humano y ordenador
    os.system("cls")

    mostrar_tablero(tablero)

    if humano == "O":
        turno = "Humano"
    else:
        turno = "Ordenador"

    # --------------------- lógica --------------------------------
    partida = True
    while partida:
        #
        #     # Tras cada movimiento hay que comprobar si hay empate
        #         # si lo hay, se sale de la partida y se muestra info
        #
        #     # Si es el turno de humano, mueve el humano
        #         # Cambiar el espacio vacío por la ficha de ese jugador
        #         # Comprobar si ha ganado
        #         # Si ha ganado se sale de la partida y se muestra el ganador
        #
        #     # Si es el turno del ordenador, mueve según el nivel
        #         # Cambiar el espacio vacío por la ficha de ese jugador
        #         # Comprobar si ha ganado
        #         # Si ha ganado se sale de la partida y se muestra el ganador        #
        #
        # jugando = seguir_jugando()  # true o false. Si es false, se sale

        if tablero_lleno(tablero):
            print("                     Empate")
            partida = False  # salida del bucle

        elif turno == "Humano":
            casilla = movimiento_jugador(tablero)
            tablero[casilla] = humano
            turno = "Ordenador"
            os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero, humano):
                print("                     Has ganado....")
                partida = False

        elif turno == "Ordenador":
            print("     El ordenador está pensando...")
            time.sleep(2)
            if nivel == 1:
                casilla = movimiento_ordenador_facil(tablero, humano)
            elif nivel == 2:
                casilla = movimiento_ordenador_dificil()
            tablero[casilla] = ordenador
            turno = "Humano"
            os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero, ordenador):
                print("                     Has perdido....")
                partida = False

    jugando = seguir_jugando()
