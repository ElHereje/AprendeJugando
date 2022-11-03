"""
Para un juego que va a tener 20.000 planetas necesitamos formar nombres
para cada uno de ellos. Crea una lista con todos los nombres de 3 sílabas
que se pueden formar con 10 consonantes y 5 vocales, de tal forma que se
intercambien consonante y vocal, y no se repita ninguna letra en cada nombre.
Al final muestra la cantidad de nombres y muestra 10 al azar.

En este caso, serían unas VARIACIONES SIN repetición

Consonantes: Variaciones de 10 elementos tomados de 3 en 3.
Vocales: Variaciones de 5 elementos tomados de 3 en 3
TOTAL = Consonantes * Vocales

10! / (10-3)! = 10*9*8 = 720
5! / (5-3)! = 5*4*3 = 60

TOTAL = 720 * 60 = 43200 nombres

"""
import random

consonantes = "bdklnprstz"
vocales = "aeiou"
nombres = []

for c1 in consonantes:
    for v1 in vocales:
        for c2 in consonantes:
            for v2 in vocales:
                for c3 in consonantes:
                    for v3 in vocales:
                        # como no se pueden repetir...
                        if (c1!=c2 and c1!=c3 and c2!=c3 and
                            v1!=v2 and v1!=v3 and v2!=v3):
                            nombre = c1+v1+c2+v2+c3+v3
                            nombres.append(nombre)
                            # como prueba:
                            # print(nombre)
print(f"Se han formado {len(nombres)} nombres")
print(f"Una muestra: ")
for i in range(1, 11):
    planeta = random.choice(nombres)
    print(f"Planeta {i} : {planeta}")

