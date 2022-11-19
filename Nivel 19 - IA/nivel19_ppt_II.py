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


def dibujo(jugada):
    """Muestra en pantalla el dibujo de la opción elegida"""
    if jugada == "Piedra":
        print("                        @@")
        print("                       @@@")
    elif jugada == "Papel":
        print("                       ===")
        print("                       ===")
    elif jugada == "Tijeras":
        print("                        |/")
        print("                        OO")


def panel_puntuacion(puntos_jugador, puntos_ordenador, numero_jugada):
    """Panel con el nº de jugadas hechas y la puntuación de cada jugador"""
    os.system("cls")

    print()
    print(f"       PIEDRA, PAPEL, TIJERAS:  {numero_jugada} de 10")
    print("      ----------------------------------")
    print(f"       PUNTOS    tú: {puntos_jugador} - Ordenador: {puntos_ordenador}")
    print("      ----------------------------------")
    print()


def comprobar_ganador(jugador, ordenador):
    """Devuelve el ganador de la tirada"""

    if jugador == "Piedra":
        if ordenador == "Piedra":
            ganador = "Ninguno"
        elif ordenador == "Papel":
            ganador = "Ordenador"
        else:
            ganador = "Humano"
    elif jugador == "Papel":
        if ordenador == "Piedra":
            ganador = "Humano"
        elif ordenador == "Papel":
            ganador = "Ninguno"
        else:
            ganador = "Ordenador"
    elif jugador == "Tijeras":
        if ordenador == "Piedra":
            ganador = "Ordenador"
        elif ordenador == "Papel":
            ganador = "Humano"
        else:
            ganador = "Ninguno"

    return ganador


def movimiento_jugador():
    """Pide al jugador humano que realice su jugada"""
    """Devuelve la jugada que hace el jugador"""

    opciones_humano = ['Piedra', 'Papel', 'Tijeras']
    jugada = ""
    while jugada not in opciones_humano:
        jugada = input("             Haz tu jugada: ").capitalize()
    else:
        return jugada


def movimiento_ordenador_con_ia(jugadas_humano, ultimo_resultado):
    """Devuelve la jugada del ordenador con IA"""
    # jugadas_humano = registro de jugadas
    # ultimo_resultado = 1 (victoria), 0 (derrota)

    if ultimo_resultado == 1:  # humano gana
        # comprobamos la última tirada --> [-1]
        if jugadas_humano[-1] == "Piedra":  # En la siguiente ronda sacará piedra o tijeras
            jugada = random.choice(["Papel", "Piedra"])
        elif jugadas_humano[-1] == "Papel":  # En la siguiente ronda sacará papel o piedra
            jugada = random.choice(["Tijeras", "Papel"])
        elif jugadas_humano[-1] == "Tijeras":  # En la siguiente ronda sacará tijeras o papel
            jugada = random.choice(["Piedra", "tijeras"])
    elif ultimo_resultado == 0:  # humano pierde
        # comprobamos la última tirada --> [0]
        if jugadas_humano[0] == "Piedra":  # En la siguiente ronda sacará papel o tijeras
            jugada = random.choice(["tijeras", "Piedra"])
        elif jugadas_humano[0] == "Papel":  # En la siguiente ronda sacará tijeras o piedra
            jugada = random.choice(["Piedra", "Papel"])
        elif jugadas_humano[0] == "Tijeras":  # En la siguiente ronda sacará piedra o papel
            jugada = random.choice(["Papel", "Tijeras"])

    return jugada


################ Programa Principal ########################

# Flujo del programa

puntos_jugador = 0
puntos_ordenador = 0
numero_jugada = 1
jugadas_humano = ['Piedra']  # la lógica es que empiece por el ppio
ultimo_resultado = 1  # suponemos parte de una situación ganadora

while True:
    panel_puntuacion(puntos_jugador, puntos_ordenador, numero_jugada)
    jugada_humano = movimiento_jugador()
    jugada_ordenador = movimiento_ordenador_con_ia(jugadas_humano, ultimo_resultado)
    ganador = comprobar_ganador(jugada_humano, jugada_ordenador)
    # ---------------------------------------------------------
    print()
    dibujo(jugada_humano)
    print()
    dibujo(jugada_ordenador)
    print()
    print("              El ordenador:", jugada_ordenador)
    print()
    # ---------------------------------------------------------
    numero_jugada += 1
    jugadas_humano.append(jugada_humano)

    if ganador == "Humano":
        puntos_jugador += 1
        ultimo_resultado = 1
        print("                     Ganas tú.")
        print()
    elif ganador == "Ordenador":
        puntos_ordenador += 1
        ultimo_resultado = 0
        print("                 Gana el ordenador.")
    elif ganador == "Ninguno":
        print("                     Empate.")
        print()

    input("         Enter para continuar...")
    # ---------------------------------------------------------
    if numero_jugada == 10:
        panel_puntuacion(puntos_jugador, puntos_ordenador, numero_jugada)
        mensaje1 = "FIN DE LA PARTIDA"
        if puntos_jugador > puntos_ordenador:
            mensaje2 = "   HAS GANADO"
        elif puntos_jugador < puntos_ordenador:
            mensaje2 = "GANA EL ORDENADOR"
        else:
            mensaje2 = "     EMPATE"
        print()
        print()
        print(f"                {mensaje1}")
        print(f"                {mensaje2}")
        print()
        print()
        print()

        break  # para salir del bucle ppal

        # -----------------------------------------------------------