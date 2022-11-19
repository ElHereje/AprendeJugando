"""
Tres en raya con IA

Tendrá 2 niveles.
Este archivo solo contiene el planteamiento y la lógica
"""

import random, time, os

def presentacion1():
    """Devuelve el nivel en el que se quiere jugar"""
    pass

def presentacion2():
    """Devuelve la ficha elegida por el humano y ordenador"""
    pass

def mostrar_tablero():
    """Muestra el tablero con las casillas vacías y puestas"""
    pass

def seguir_jugando():  # true o false
    """True si quieres seguir, false si no"""
    pass

def hay_ganador(tablero, jugador):
    """Comprueba si un estado del tablero es ganador"""
    '''(comprueba si hay 3 fichas en línea'''
    pass

def tablero_lleno(tablero):  # true o false
    """Devuelve si está lleno o vacío"""
    """Si está lleno, significa empate"""
    pass

def casilla_libre(tablero, casilla):
    """True si una casilla dada esta vacía y false si no"""
    pass

def movimiento_jugador(tablero):
    """Devuelve la casilla elegida por el jugador humano"""
    pass

def movimiento_ordenador_facil(tablero, jugador):
    """El ordenador solo se defiende de ser ganado en la siguiente jugada"""
    '''es decir, solo bloqueará el posible peligro'''
    pass



#######################  PROGRAMA PPAL  #######################

jugando = True

while True:
    # definimos el tablero
    tablero = [" "] * 9  # lista con 9 espacios vacíos

    # ------------------------------------------------------
    # elejir nivel y ficha(turno)

    # ------------------------------------------------------
    # partida = True
    # while partida:

        # Si es el turno de humano, mueve el humano
            # Cambiar el espacio vacío por la ficha de ese jugador
            # Comprobar si ha ganado
            # Si ha ganado se sale de la partida y se muestra el ganador

        # Si es el turno del ordenador, mueve según el nivel
            # Cambiar el espacio vacío por la ficha de ese jugador
            # Comprobar si ha ganado
            # Si ha ganado se sale de la partida y se muestra el ganador

        # Tras cada movimiento hay que comprobar si hay empate
            # si lo hay, se sale de la partida y se muestra info

    # jugando = seguir_jugando()  # true o false. Si es false, se sale

