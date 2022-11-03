'''
Calcula la suma de los números del 1 al 1 millón
Hacerlo con while y for y mide el tiempo de cada uno.
Usar perf_counter()
'''
import time
from time import perf_counter

suma = 0
inicio = perf_counter()
for i in range(1, 1_000_001):  # guiones para identificar bien el nº
    suma += i
final = perf_counter()
tiempo = final - inicio

print(f"Suma = {suma}")
print(f"Tiempo con FOR --> {tiempo} segundos")

suma2 = 0
j = 0
inicio2 = perf_counter()
while j <= 1000000:
    suma2 += j
    j += 1
final2 = perf_counter()
tiempo2 = final2 - inicio2
print(f"Suma = {suma2}")
print(f"Tiempo con WHILE --> {tiempo2 } segundos")
