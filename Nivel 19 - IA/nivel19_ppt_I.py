"""
Vamos a realizar el juego Piedra, papel, tijeras con IA

lo haremos frente a las tendencias de comportamiento humano

        Inteligencia artificial para Piedra, papel, Tijeras
        ---------------------------------------------------

Tendencias básicas del ser humano frente a este juego
- Si tras una jugada gana, habrá más posibilidades de que siga con la misma
- Si pierde, habrá más probabilidades de que cambie de jugada siguiendo el orden

Orden: (1)Piedra - (2)Papel - (3)Tijeras - (4)Piedra - ...

Implementación
--------------

- En el caso de que el jugador gane la última partida:
    Prever que en la siguiente elegirá la misma o la anterior (aleatorio)

- En el caso de que el jugador pierda:
    Prever que la siguiente elegirá la siguiente en el orden o la anterior
    (aleatoria)

La estrategia a seguir por la IA es que el ordenador reaccionará a las 2
opciones más probables que coja el jugador

"""

import random
import time
import os

def dibujo():
    '''Muestra en pantalla el dibujo de la opción elegida'''
    pass

def panel_puntuacion():
    '''Panel con el nº de jugadas hechas y la puntuación de cada jugador'''
    pass

def comprobar_ganador():
    '''Devuelve el ganador de la tirada'''
    pass

def movimiento_jugador():
    '''Devuelve la jugada que hace el jugador'''
    pass

def movimiento_ordenador_con_ia():
    '''Devuelve la jugada del ordenador con IA'''
    pass

################ Programa Principal ########################

# Flujo del programa


# -----------------------------------------------------------