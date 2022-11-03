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

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
elegido = ""
salir = False
muertos = 0
intentos = 15
errores = []

while len(elegido) < 4:
    n  = random.choice(num)
    if n not in elegido:
        elegido += n
print(elegido)  # --> control


print()
print("BIENVENIDO A MASTERMIND")
print("--------------------------------------------------")
print()
print("Se ha generado un nº de 4 cifras DISTINTAS que debes adivinar.")


while muertos != 4 or intentos != 0:
    heridos = 0
    muertos = 0
    elige = input("Introduce un número de 4 cifras. Q para salir : ")
    if elige == "q":
        print(f"El código a acertar era {elegido}")
        break
    else:
        if len(elige) == 4:
            print(elige)
            for i in range(len(elegido)):
                if elige[i] in elegido:
                    heridos += 1
                if elige[i] == elegido[i]:
                    muertos += 1
                i += 1
            if elige in errores:
                print("Ese nº ya estaba registrado. Pierdes un intento")
            elif muertos == 4:
                print(f"HAS acertado todos los números --> {elegido}")
                print(f"Lo has conseguido en {16 - intentos} intentos.")
                print("FIN DEL JUEGO")
                break

            errores.append(elige)
            intentos -= 1
            print(f"Heridos = {heridos}. Muertos = {muertos}. Te quedan {intentos} intentos")
            elige = ""
        else:
            print("DATOS ERRÓNEOS")








