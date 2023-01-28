'''Definir 2 funciones para calcular la suma del 1 a n números.
Una de ellas sumando uno a uno, y otra aplicando la fórmula de gauss:


import time

def suma_lineal(n):
    pass

def suma_constante(n):
    pass
    
cantidad = 1000000

for i in range(4):
    
    t0 = time.time()
    suma1 = suma_lineal(cantidad)
    t1 = time.time()
    suma2 = suma_constante(cantidad)
    t2 = time.time()
    
    print(f"{suma1} - {t1-t0}")
    print(f"{suma2} - {t2-t1}")
    
    cantidad *= 10 # multiplicamos la cantidad por 10 en la siguiente iteración'''
    

import time

def suma_lineal(n):
    suma = 0
    for i in range(cantidad + 1): # (1, n+1)
        suma = suma + i
    return suma
def suma_constante(n):
    suma = (n/2) * (n+1)
    return suma
    
cantidad = 1000000

for i in range(4):
    
    t0 = time.time()
    suma1 = suma_lineal(cantidad)
    t1 = time.time()
    suma2 = suma_constante(cantidad)
    t2 = time.time()
    
    print(f"Para {cantidad} : ")
    print(f"{suma1} - {t1-t0} segundos")
    print(f"{suma2} - {t2-t1} segundos")
    print()
    
    cantidad *= 10 # multiplicamos la cantidad por 10 en la siguiente iteración
    
'''
Se aprecia que independientemente del resultado en la lineal el tiuempo crece de
manera lineal al contrario que la constante.

la notación asintótica permite representar la cantidad de operaciones que necesita
un algoritmo para una cantidad de datos de entrada.

hay varios tipos:
* O grande (omicrom)
* Ω grande (omega)
* θ grande (theta )

Se puede aplicar a complejidad de tiempo y complejidad de espacio
Nosotros nos vamos a centrare en complejidad de tiempo.
en los casos anterires:

* la suma_lineal es de complejidad lineal --> 0(n)
* la suma_constante es de complejidad constante --> 0(1)

'''