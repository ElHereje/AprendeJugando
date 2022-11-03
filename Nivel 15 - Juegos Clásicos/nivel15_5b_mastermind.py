'''
Juego Mastermind (o también llamado muertos y heridos)

1. Presentación. Usuario tiene que adivinar número antes de 15 intentos.
2. Generar número aleatorio de 4 cifras (han de ser distintos).
3. Pedir al usuario un número de 4 cifras distintas.
4. Comparar el número del usuario con el generado:
	Si coincide en posición y valor, muertos aumenta en1
	Si solo coincide el valor y no la posición, heridos aumenta en 1.
5. Mostrar el número de muertos y heridos conseguidos.
6. Seguir pidiendo números al usuario.
7. Mostrar siempre todos los números y resultados dichos hasta ahora.
8. Si acierta los 4 números, mostrar mensaje de victoria y finalizar.
9. Más de 15 intentos, mostrar mensaje de derrota y finalizar.
10 Opción de salir en cualquier momento y mostrar el número.
'''


# ARCHIVO: mastermind5.py

# modulo que va a permitir elegir números aleatoriamente
import random

# el conjunto de símbolos válidos en el código*
from past.builtins import raw_input

digitos = ('0','1','2','3','4','5','6','7','8','9')

# "elegimos" el código
cant_digitos = 4
codigo = ''
for i in range(cant_digitos):
    candidato = random.choice(digitos)
    # vamos eligiendo digitos no repetidos
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

# iniciamos interacción con el usuario
print ("Bienvenido/a al Mastermind!")
print (f"Tienes que adivinar un numero de {cant_digitos} cifras distintas")
propuesta = input("¿Que código propones?: ")

# procesamos las propuestas e indicamos aciertos y coincidencias
intentos = 1
while propuesta != codigo and propuesta != "Me doy":
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0

    # recorremos la propuesta y verificamos en el codigo
    for i in range(cant_digitos):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    print ("Tu propuesta (", propuesta, ") tiene", aciertos, \
          "aciertos y ", coincidencias, "coincidencias.")
    # pedimos siguiente propuesta
    propuesta = input("Propón otro código: ")

if propuesta == "Me doy":
    print (f"El código era:  {codigo}")
    print ("Suerte la proxima vez!")
else:
    print (f"Felicitaciones! Adivinaste el código en {intentos} intentos.")

