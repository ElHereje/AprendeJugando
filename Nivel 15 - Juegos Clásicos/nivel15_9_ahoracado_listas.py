import random
import os


palabras = ["CARAMELO", "CAFETERA", "MARIPOSA", "CARRETERA", "TERMOMETRO",
            "ESCALERA", "CRUCIGRAMA", "MICROONDAS", "PARTITURA", "ELEFANTE",
            "CARNICERO", "PEGAMENTO", "CIRUJANO", "MERMELADA", "ETIQUETA",
            "HERRAMIENTA", "ARMARIO", "HOGUERA", "ASCENSOR", "BELLOTA"]

# elegimos una palabra aleatoria de la lista palabras y la convertimos
# también en una lista

palabra = list(random.choice(palabras))

horca =        ["           !=======N",
                "                  N",
                "                  N",
                "                  N",
                "                  N",
                "                  N",
                "                  N",
                "      ____________N"]

ahorcado =         ["          !=======N",
                    "          O       N",
                    "       /  |  \    N",
                    "       \  |  /    N",
                    "        /   \     N",
                    "       /     \    N",
                    "      _\     /_   N",
                    "     _____________N"]

#  Creamos las variables donde almacenamos las letras

letras_todas = []
fallos = 1  # para que empiece por la 1ª linea
resultado = []   # lista con guiones a sustituir por palabras

for i in range(len(palabra)):
    resultado.append("_")  # sustituimos las letras de la palabra x guiones

# bucle principal del juego

while True:

    os.system("cls")

    print("***   JUEGO DEL AHORACADO   ***")
    print(("*************************************"))

    for i in range(fallos):
        print(ahorcado[i])  # mostramos tantos elementos como fallos
    for i in range(len(horca)-fallos):
        print(horca[i+fallos])  # para mostrar el resto de elementos
    print()

    # mostramos el resultado que se va obteniendo

    print("     ", end=" ")
    for i in resultado:
        print(i, end=" ")
    print()
    print()
    # Comprobamos si has acertado o terminado los intentos:

    if resultado == palabra:
        print("***   HAS GANADO   ***")
        print()
        break

    if fallos > 6:
        print("La palabra era... ","".join(palabra)) # volvemos a convertir la lista en cadena
        print("***   HAS PERDIDO   ***")
        print()
        break

    # Bucle para pedir letras:

    while True:
        letra_usuario_sin_formato = input("Dime una letra.. : ")
        letra_usuario = letra_usuario_sin_formato.upper()
        if len(letra_usuario) != 1:
            print("Introduce UNA letra... ")
        elif letra_usuario in letras_todas:
            print("Esa letra ya la has dicho...")
        elif letra_usuario not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            print("Introduce una LETRA...")
        else:
            letras_todas.append(letra_usuario)
            break  # para salir de este bucle y volver al ppal

    # Comprobamos si la letra está en la palabra. Si lo está, la sustituimos
    # por el guion

    for i in range(len(palabra)):
        if palabra[i] == letra_usuario:
            resultado[i] = letra_usuario

    if letra_usuario not in palabra:
        fallos += 1

    print()
    print()




