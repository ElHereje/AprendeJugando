# Vamos a ver las dificultades al trabajar con bucles for anidados
"""
Programa que adivina una clave mediante fuerza bruta.
--> La clave consiste en 4 letras minúsculas <--
"""

import time

clave = input("Dime una clave de 4 letras: ")
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
inicio = time.time()

for l1 in alfabeto:
    for l2 in alfabeto:
        for l3 in alfabeto:
            for l4 in alfabeto:
                intento = l1+l2+l3+l4
                if intento == clave:
                    print(f"Clave encontrada: {clave}")

final = time.time()
print(f"Tiempo consumido: {final-inicio} segundos")

# en el caso de 5 letras:

clave = input("Dime una clave de 5 letras: ")
for l1 in alfabeto:
    for l2 in alfabeto:
        for l3 in alfabeto:
            for l4 in alfabeto:
                for l5 in alfabeto:
                    intento = l1 + l2 + l3 + l4 + l5
                    if intento == clave:
                        print(f"Clave encontrada: {clave}")

final = time.time()
print(f"Tiempo consumido: {final-inicio} segundos")

# en el caso de un alfabeto de 64 caracteres:

alfabeto = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ1234567890"

clave = input("Dime una clave de 5 letras (MAY Y MIN): ")
for l1 in alfabeto:
    for l2 in alfabeto:
        for l3 in alfabeto:
            for l4 in alfabeto:
                for l5 in alfabeto:
                    intento = l1 + l2 + l3 + l4 + l5
                    if intento == clave:
                        print(f"Clave encontrada: {clave}")

final = time.time()
print(f"Tiempo consumido: {final-inicio} segundos")

# Se ve que el tiempo empleado aumenta de manera exponencial al aumentar
# el tamaño de la contraseña. De todas formas, aunque la encuentre antes
# de tiempo, aún no acaba el programa, ya que tienen que finalizar los bucles for
#



