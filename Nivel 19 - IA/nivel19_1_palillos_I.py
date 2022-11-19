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

En esta primera parte vamos a estructurar el progama

"""

# importamos los módulos necesarios
import random
import time
import os  # para limpiar la pantalla


def presentacion_1():
    """Mostramos pantalla de inicio y devuelve
        el nivel fácil o difícil que elije el usuario"""
    pass


def presentacion_2():
    """Mostramos una segunda pantalla con los datos del juego,
        y pedimos al usuario que de enter para empezar"""
    pass


def sorteo_opciones():
    """devuelve dos valores aleatorios: Nº de palillos
            (entre 16 y 23) y nº de palillos a quitar (entre 3 y 5)"""
    pass


def area_de_juego():
    """Muestra los palillos que hay en cada jugada de la partida"""
    pass


def movimiento_jugador():
    """Devuelve el nº de palillos que el usuario quita en cada jugada"""
    pass


def movimiento_ordenador_aleatorio():
    """Devuelve nº aleatorio de palillos a quitar como jugada del ordenador"""
    pass


def movimiento_ordenador_ia():
    """Devuelve nº aleatorio de palillos a quitar como jugada del ordenador
        calculados para que el ordenador gane siempre que pueda """
    pass


def mostrar_ganador():
    """Muestra pantalla final con ganador de a partida"""
    pass

# ---------------------- Programa Ppal --------------------------------------


# flujo del programa


# ----------------------------------------------------------------------------
