"""Juego de memoria. Te muestra 4 colores y te da 3 segundos
para recordarlos en el orden que aparecieron. Si aciertas te
los vuelve a mostrar en otro orden para empezar de nuevo.
"""

import random
from time import sleep

colores = ["rojo", "verde", "azul",
           "gris", "amarillo", "rosa",
           "lila", "negro", "blanco"]

puntos = 0
muestra = random.sample(colores, 4)

while True:
    print("MEMORIZA LOS COLORES !!!")
    print("Cuando aparezcan, tendrás cuatro segundos para memorizarlos...")
    print()
    print("... Preparado ...")
    sleep(1)
    print("......listo .....")
    sleep(1)
    print("........Ya.......")
    print()
    for i in range(len(muestra)):
        print(" ", muestra[i], end=" ")
    sleep(4)
    print()

    for i in range(10):
        print("*" * i * 5)
    for i in range(10, 0, -1):
        print("*" * i * 5)

    color_1 = input("Primero: ")
    color_2 = input("Segundo: ")
    color_3 = input("Tercero: ")
    color_4 = input("Cuarto: ")

    if (color_1 == muestra[0]) and (color_2 == muestra[1]) and (color_3 == muestra[2]) and (color_4 == muestra[3]):
        puntos += 1
        print(f"Has acertado.. tienes {puntos} puntos.")
        muestra = random.sample(colores, 4)
        print()
    else:
        print(f"Orden erróneo... has conseguido {puntos} puntos...")
        print("Fin del juego")
        break
