"""
Comprobar si la suma de 2 números de una lista dán
como resultado 10, y mostrar todas las soluciones.
(no cuentan la suma de un nº consigo mismo)
"""
import time

numeros = [2, 3, 5, 8, 4, 7, 6, 5, 1]

# creamos otra lista (parejas)
parejas = []

for i in range(len(numeros)):
    for j in range(len(numeros)):
        if  (i != j) and (numeros[i] + numeros[j] == 10):
            pareja = sorted([numeros[i], numeros[j]])
            if pareja not in parejas:
                parejas.append(pareja)
print(parejas)


# como esto requiere de dos bucles for, no es muy eficiente, por lo que
# otra opción sería:
# el 1er numero lo comparamos con el resto, pero el segundo ya no hace
# falta compararlo con el primero, porque ya se ha hecho...

for i in range(len(numeros) - 1):
    for j in range(i+1, len(numeros)):
        if numeros[i] + numeros[j] == 10:
            pareja = sorted([numeros[i], numeros[j]])
            if pareja not in parejas:
                parejas.append(pareja)
print(parejas)

# es mas eficiente, pero sigue teniendo 2 bucles for.
# una forma mas óptima sería

for n in numeros:
    # restringimos que no se valore con sigo mismo a través de una copia de la lista
    copia = list(numeros)
    copia.remove(n)
    if 10-n in copia:
        pareja = sorted([n, 10-n])
        if pareja not in parejas:
            parejas.append(pareja)
print(parejas)


# También se podría haber hecho sin hacer una copia, con el método index:
parejas2 = []

for i in range(len(numeros)):
    sumando = 10 - numeros[i]
    if sumando in numeros and numeros.index(sumando) != i:
        pareja = sorted([numeros[i], sumando])
        if pareja not in parejas2:
            parejas2.append(pareja)
print(parejas2)

