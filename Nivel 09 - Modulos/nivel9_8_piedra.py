# piedra, papel o tijeras...


'''
jugando = True
while jugando:
    CODIGO

    print("Jugamos una partida")
    seguir = input("Quieres volver a jugar (s/n)?: ")
    if seguir == "n"
    jugando = False
'''

import random

jugando = True
opciones = ["piedra", "papel", "tijeras"]
while jugando:
    ordenador = random.choice(["piedra", "papel", "tijeras"])
    mi_salida = input("Elige...piedra, papel o tijeras: ")

    if mi_salida == ordenador:
        print(f"También he sacado {ordenador}...")
    elif ordenador == "piedra":
        if mi_salida == "papel":
            print(f"He sacado {ordenador}...Has Ganado")
        elif mi_salida == "tijeras":
            print(f"He sacado {ordenador}...Has Perdido")
    elif ordenador == "papel":
        if mi_salida == "piedra":
            print(f"He sacado {ordenador}...Has Perdido")
        elif mi_salida == "tijeras":
            print(f"He sacado {ordenador}...Has Ganado")
    elif ordenador == "tijeras":
        if mi_salida == "papel":
            print(f"He sacado {ordenador}...Has Ganado")
        elif mi_salida == "piedra":
            print(f"He sacado {ordenador}...Has Perdido")
    if mi_salida not in opciones:
        print("No te entiendo...")

    seguir = input("Quieres volver a jugar (s/n)?: ")
    if seguir == "n":
        jugando = False


