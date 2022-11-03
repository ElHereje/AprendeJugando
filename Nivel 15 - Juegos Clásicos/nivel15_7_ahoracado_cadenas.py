"""
Juego del ahorcado
------------------------------

1. Elegir aleatoriamente una palabra de una lista.
2. Mostrar dibujo de una horca.
3. Mostrar un guión por cada letra de la palabra.
4. Pedir al usuario una letra.
    Si no es una letra indicarlo, si ya se ha dicho indicarlo.
5. Comprobar si esa letra está en la palabra.
6. Si está, volver a cargar dibujo como estaba y sustituir guion por letra.
7. Si no está, se añade parte al dibujo y se muestran los guiones como antes.
8. Si se falla 6 veces se completa el dibujo y se indica que se ha perdido.
9. Si se acierta la palabra, indicar que se ha ganado.

"""

import random
import os
palabras = ["CARAMELO", "CAFETERA", "MARIPOSA", "CARRETERA", "TERMOMETRO",
            "ESCALERA", "CRUCIGRAMA", "MICROONDAS", "PARTITURA", "ELEFANTE",
            "CARNICERO", "PEGAMENTO", "CIRUJANO", "MERMELADA", "ETIQUETA",
            "HERRAMIENTA", "ARMARIO", "HOGUERA", "ASCENSOR", "BELLOTA"]

# elegimos una palabra aleatoria de la lista palabras

palabra = random.choice(palabras)

#  Dibujamos la horca y sus posibilidades:

fallo0 = '''
            !===N
                N
                N
                N
            =====
'''

fallo1 = '''
            !===N
            O   N
                N
                N
            =====
'''

fallo2 = '''
            !===N
           _O   N
                N
                N
            =====
'''

fallo3 = '''
            !===N
           _O_  N
                N
                N
            =====
'''

fallo4 ='''
            !===N
           _O_  N
            |   N
                N
            =====
'''

fallo5 = '''
            !===N
           _O_  N
            |   N
           /    N
            =====
'''

fallo6 = '''
            !===N
           _O_  N
            |   N
           / \  N
            =====
'''

letras_correctas = ""   # correctas dichas por el usuario
letras_todas = ""         # todas las letras dichas por el usuario
fallos = 0                     # control de fallos

#  Bucle principal del juego

while True:

    os.system("cls")

    # presentamos e iniciamos la horca con sus opciones

    print("*********************************")
    print("*** JUEGO DEL AHORCADO ***")
    print("*********************************")

    if fallos == 0:
        print(fallo0)
    elif fallos == 1:
        print(fallo1)
    elif fallos == 2:
        print(fallo2)
    elif fallos == 3:
        print(fallo3)
    elif fallos == 4:
        print(fallo4)
    elif fallos == 5:
        print(fallo5)
    elif fallos == 6:
        print(fallo6)

    print()

    resultado = ""

    for letra in palabra:
        if letra in letras_correctas:
            resultado += letra
        else:
            resultado += "_"

    print("             {}".format(resultado))
    print()
    print(f"Letras introducidas: {letras_todas}")
    print()
    print(f"Errores restantes: {5-fallos}")
    print()
    print()

    # comprobamos si se ha acertado la palabra o se han terminado los intentos

    if resultado == palabra:
        print("***         HAS GANADO       ***")
        break

    if fallos > 5:
        print("***         HAS PERDIDO      ***")
        break

    # Bucle para que el usuario teclee una letra que cumpla los requisitos

    while True:
        letra_usuario_sin_formato = input("Dime una Letra: ")
        letra_usuario = letra_usuario_sin_formato.upper()
        if len(letra_usuario) < 1 or len(letra_usuario) > 1:
            print("Introduce una letra...")
        elif letra_usuario in letras_todas:
            print("Esa letra ya la has dicho...")
        elif not letra_usuario.isalpha():
            print("Introduce una letra...")
        else:
            letras_todas += letra_usuario
            break

    # Comprobamos si la letra está en la palabra

    if letra_usuario not in palabra:
        fallos += 1
    else:
        letras_correctas += letra_usuario


