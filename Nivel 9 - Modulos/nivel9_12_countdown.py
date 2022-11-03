'''
Programa que lleva a cabo una cuenta atrás de 10 seg.
    1. Muestra cada seg (10 - 9 - 8 - ...)
    2. Muestra cada 5 décimas (10 - 9.5 - 8 - 8.5 - ...)
Mide el tiempo para comprobar que transcurren 10 seg.
'''

import time

inicio = time.time()
for i in range(10, -1, -1):
    print(f"{i} ", end="")
    time.sleep(1)
final = time.time()
print(f"\nTiempo transcurrido {final - inicio}")

inicio = time.time()
for i in range(40, 19, -1):
    print(f"{(i-20)/2} ", end="")
    time.sleep(.5)
final = time.time()
print(f"\nTiempo transcurrido {final - inicio}")
