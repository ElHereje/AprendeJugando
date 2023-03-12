# CONTINUE

"""
Programa que muestre las letras de una palabra
a excepción de la "h"
"""

palabra = "zanahoria"
for letra in palabra:
    if letra == "h":
        continue
    print(letra)

# ****************************************

"""
Programa que muestre si los nº de una lista son positivos o negativos,
a excepción del 0, que se lo salta
"""

numeros = [1, 4, -3, 5, 0, 7, -2, 6]

for num in numeros:
    if num == 0:
        continue
    if num > 0:
        print(f"{num} es positivo.")
    else:
        print(f"{num} es negativo")
