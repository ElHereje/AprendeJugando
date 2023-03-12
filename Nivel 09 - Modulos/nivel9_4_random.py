# MÉTODO RANDOM

# randint --> random.randint(inicio, fin) ambos incluidos

"""
Juego que genere número aleatorio del 1 al 100 y te pide
que los adivines.
Se indica si el número es mayor o menor.
Tienes 7 intentos.
"""

import random

jugando = True
intentos = 0
numero = random.randint(1, 100)

while jugando:
    intentos += 1
    if intentos <= 7:
        elegido = int(input("Dime un nº del 1 al 100: "))
        if elegido == numero:
            print(f"ACERTASTES a la {intentos} vez...!!!!..enhorabuena crack...")
            jugando = False
        elif elegido > numero:
            print(f"Intenta uno menor...llevas {intentos} intentos")
        elif elegido < numero:
            print(f"Intenta uno mayor...llevas {intentos} intentos")
    else:
        print(f"Se te acabaron los intentos. EL numero era {numero}")



