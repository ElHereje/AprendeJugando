"""
Juego Mastermind (o también llamado muertos y heridos)

1. Presentación. Usuario tiene que adivinar número antes de 15 intentos.
2. Generar número aleatorio de 4 cifras (han de ser distintos).
3. Pedir al usuario un número de 4 cifras distintas.
4. Comparar el número del usuario con el generado:
	1. Si coincide en posición y valor, muertos aumenta en 1.
	2. Si solo coincide el valor y no la posición, heridos aumenta en 1.
5. Mostrar el número de muertos y heridos conseguidos.
6. Seguir pidiendo números al usuario.
7. Mostrar siempre todos los números y resultados dichos hasta ahora.
8. Si acierta los 4 números, mostrar mensaje de victoria y finalizar.
9. Más de 15 intentos, mostrar mensaje de derrota y finalizar.
10 Opción de salir en cualquier momento y mostrar el número.
"""

import random
import os

digitos = "1234567890"
numero = ""
muertos = 0
heridos = 0
intento = None  # --> numero indicado por el usuario
intentos = []
salir = False

#  Presentación del programa

print("**************************************")
print("*                                    *")
print("*       Juego Muerto y Heridos       *")
print("*           Tienes 15 intentos       *")
print("*                                    *")
print("        Pulsa ENTER para empezar     *")
print("*                                    *")
print("**************************************")

input()  # se detiene el programa a la espera de "enter"

#  Generamos  número aleatorio:

while len(numero) < 4:
    digito = random.choice(digitos)
    if digito not in numero:
        numero += digito


# Bucle principal mientras no se acierte el número.

while True:
    os.system("cls")

    print(numero)  # control
    print("*****************************************************")
    print("*                    MUERTOS Y HERIDOS              *")
    print("*****************************************************")
    print("*          NUMERO          -        M  -  H         *")
    print("*       --------------            ------------      *")

    # Mostramos los intentos del usuario:

    for i in range(len(intentos)):
        plantilla = "*           {}          -         {}  -  {}         *"
        print(plantilla.format(intentos[i][0], intentos[i][1], intentos[i][2]))
    print("*                                                   *")

    # Comprobación si se ha ganado:

    if numero == intento:
        print("*        Has acertado el número. Has ganado.        *")
        print(f"*            Has necesitado {len(intentos)} intentos             *")
        print()
        break

    # Comprobación de los intentos y salida si agotados:

    if len(intentos) >= 15:
        print("*    Has agotado todos los intentos. Has perdido    *")
        print(f"                     El número era {numero}                     *")
        break

    # Bucle para que el usuario elija un número correcto:

    while True:
        intento = input("=> Introduce intento ('q' para salir): ")
        if intento == "q":
            salir = True
            break
        elif len(intento) < 4 or len(intento) > 4:
            print("Introduce un número de 4 dígitos...")
        elif intento[0] not in digitos or intento[1] not in digitos or \
                intento[2] not in digitos or intento[3] not in digitos:
            print("Introduce solo números del 0 al 9.")
        elif intento[0] == intento[1] or intento[0] == intento[2] or intento[0] == intento[3] or \
                intento[1] == intento[2] or intento[1] == intento[3] or intento[2] == intento[3]:
            print("No se pueden repetir números")
        else:
            break  # salimos de este bucle e intento se queda con lo introducido por el usuario

    #  Si la bandera de salir es True, salimos:

    if salir:
        print(f"La  solución era {numero}")
        break

    # Bucle para comprobar los muertos y heridos.

    for i in range(4):
        if intento[i] in numero:
            if intento[i] == numero[i]:
                muertos += 1
            else:
                heridos += 1

    # Añadimos el intento y resultado a la lista de intentos

    intentos.append([intento, muertos, heridos])

    # Reiniciamos de nuevo las variables

    muertos = 0
    heridos = 0



