'''
Hallar la suma del doble de l0s elementos pares de la lista
'''

datos = [3, 8, 11, 16, 21, 24]

# programación imperativa
suma = 0
for dato in datos:
    if dato % 2 == 0:
        suma += dato*2
print(f"La suma del soble de los pares de la lista es {suma}")


# programación funcional (no hay bucles. Se devuelve el valor directa\)¡
from functools import reduce

suma2 = reduce(lambda x, y: x+y, map(lambda x: x*2, filter(lambda x: x%2==0, datos)))
print(f"De manera funcional, la suma sale {suma2}")

# método sencillo con listas de comprensión
suma3 = sum([x*2 for x in datos if x%2==0])
print(f"Con listas por Comprensión sale {suma3}")