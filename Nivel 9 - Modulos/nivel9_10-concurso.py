# CONCURSO MATEMÁTICO.

# HAY QUE HACER TODAS LAS OPERACIONES POSIBLES EN 10 SEG.

import random
import time

print()
print("********** CONCURSO MATEMÁTICO **********")
print()
print(" Haz todas las operaciones que puedas.")
print("      tienes 10 segundos....")
print()
print("*****************************************")
print()
input("Para empezar pulsa enter....")

puntos = 0
inicio = time.time()
resultado = " "

while True:
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    op = random.choice(["+", "X"])

    if op == "+":
        resultado = n1 + n2
        print(n1, op, n2, end=" ")  # el end es para que no salte de línea
    elif op == "X":
        resultado = n1 * n2
        print(n1, op, n2, end=" ")

    respuesta = int(input("= "))

    if respuesta == resultado:
        puntos += 1
        print(f"Respuesta correcta... tienes {puntos} puntos")
    else:
        print(f"Respuesta incorrecta... tienes {puntos} puntos")

    final = time.time()
    if final - inicio >= 10:
        print("SE ACABÓ EL TIEMPO....")
        break

print("juego terminado....")
print(f"Has acumulado {puntos} puntos....")
